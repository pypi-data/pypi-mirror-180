from ast import literal_eval
from base64 import b64decode, b64encode
from ipaddress import ip_network, ip_address
from urllib.request import urlopen
from urllib.parse import urlencode
import json
import os
import socket
from shutil import copy2, which
from subprocess import call
import sys
from tempfile import TemporaryDirectory
from time import time
from uuid import UUID
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import urllib.request
import yaml

# colors = {'blue': '36', 'red': '31', 'green': '32', 'yellow': '33', 'pink': '35', 'white': '37'}


def error(text):
    color = "31"
    print(f'\033[0;{color}m{text}\033[0;0m')


def warning(text):
    color = "33"
    print(f'\033[0;{color}m{text}\033[0;0m')


def info(text):
    color = "36"
    print(f'\033[0;{color}m{text}\033[0;0m')


def success(text):
    color = "32"
    print(f'\033[0;{color}m{text}\033[0;0m')


def get_overrides(paramfile=None, param=[]):
    """

    :param paramfile:
    :param param:
    :return:
    """
    overrides = {}
    if paramfile is not None:
        if not os.path.exists(os.path.expanduser(paramfile)):
            error(f"Parameter file {paramfile} not found. Leaving")
            os._exit(1)
        with open(os.path.expanduser(paramfile)) as f:
            try:
                overrides = yaml.safe_load(f)
            except:
                error(f"Couldn't parse your parameters file {paramfile}. Leaving")
                os._exit(1)
    if param is not None:
        for x in param:
            if len(x.split('=')) < 2:
                continue
            else:
                if len(x.split('=')) == 2:
                    key, value = x.split('=')
                else:
                    split = x.split('=')
                    key = split[0]
                    value = x.replace(f"{key}=", '')
                if value.isdigit():
                    value = int(value)
                elif value.lower() == 'true':
                    value = True
                elif value.lower() == 'false':
                    value = False
                elif value == '[]':
                    value = []
                elif value.startswith('{') and value.endswith('}') and not value.startswith('{\"ignition'):
                    value = literal_eval(value)
                elif value.startswith('[') and value.endswith(']'):
                    if '{' in value:
                        value = literal_eval(value)
                    else:
                        value = value[1:-1].split(',')
                        for index, v in enumerate(value):
                            v = v.strip()
                            value[index] = v
                overrides[key] = value
    return overrides


def get_token(token, offlinetoken=None):
    aihome = f"{os.environ['HOME']}/.aicli"
    url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    if token is not None:
        segment = token.split('.')[1]
        padding = len(segment) % 4
        segment += padding * '='
        expires_on = json.loads(b64decode(segment))['exp']
        remaining = expires_on - time()
        if expires_on == 0 or remaining > 600:
            return token
    data = {"client_id": "cloud-services", "grant_type": "refresh_token", "refresh_token": offlinetoken}
    data = urlencode(data).encode("ascii")
    result = urlopen(url, data=data).read()
    page = result.decode("utf8")
    token = json.loads(page)['access_token']
    with open(f"{aihome}/token.txt", 'w') as f:
        f.write(token)
    return token


def confirm(message):
    message = f"{message} [y/N]: "
    try:
        _input = input(message)
        if _input.lower() not in ['y', 'yes']:
            error("Leaving...")
            sys.exit(1)
    except:
        sys.exit(1)
    return


def match_mac(host, mac):
    if ':' not in mac or 'inventory' not in host:
        return False
    found = False
    for interface in json.loads(host['inventory'])['interfaces']:
        if interface.get('mac_address', '') == mac:
            found = True
            break
    return found


def valid_uuid(uuid):
    try:
        UUID(uuid)
        return True
    except:
        return False


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    result = s.getsockname()[0]
    s.close()
    return result


def create_onprem(overrides={}, debug=False):
    if which('podman') is None:
        error("You need podman to run this")
        sys.exit(1)
    with TemporaryDirectory() as tmpdir:
        with open(f"{tmpdir}/pod.yml", 'w') as p:
            pod_url = "https://raw.githubusercontent.com/openshift/assisted-service/master/deploy/podman/pod.yml"
            response = urllib.request.urlopen(pod_url)
            p.write(response.read().decode('utf-8'))
        with open(f"{tmpdir}/configmap.yml.ori", 'w') as c:
            cm_name = 'okd-configmap' if overrides.get('okd', False) else 'configmap'
            cm_url = f"https://raw.githubusercontent.com/openshift/assisted-service/master/deploy/podman/{cm_name}.yml"
            response = urllib.request.urlopen(cm_url)
            c.write(response.read().decode('utf-8'))
        ip = overrides.get('ip') or get_ip() or '192.168.122.1'
        info(f"Using ip {ip}")
        IMAGE_SERVICE_BASE_URL = f'http://{ip}:8888'
        SERVICE_BASE_URL = f'http://{ip}:8090'
        with open(f"{tmpdir}/configmap.yml", 'wt') as dest:
            for line in open(f"{tmpdir}/configmap.yml.ori", 'rt').readlines():
                if 'IMAGE_SERVICE_BASE_URL' in line:
                    dest.write(f"  IMAGE_SERVICE_BASE_URL: {IMAGE_SERVICE_BASE_URL}\n")
                elif 'SERVICE_BASE_URL:' in line:
                    dest.write(f"  SERVICE_BASE_URL: {SERVICE_BASE_URL}\n")
                else:
                    dest.write(line)
        if overrides.get('keep', False):
            copy2(f"{tmpdir}/configmap.yml", '.')
            copy2(f"{tmpdir}/pod.yml", '.')
        else:
            if debug:
                print(open(f"{tmpdir}/configmap.yml").read())
                info(f"Running: podman play kube --configmap {tmpdir}/configmap.yml {tmpdir}/pod.yml")
            call(f"podman play kube --configmap {tmpdir}/configmap.yml {tmpdir}/pod.yml", shell=True)


def delete_onprem(overrides={}, debug=False):
    if which('podman') is None:
        error("You need podman to run this")
        sys.exit(1)
    if debug:
        info("Running: podman pod rm -fi assisted-installer")
    call("podman pod rm -fi assisted-installer", shell=True)


def get_relocatable_data(baremetal_cidr='192.168.7.0/24', overrides={}):
    sno = overrides.get('high_availability_mode', 'XXX') == "None" or overrides.get('sno', False)
    basedir = f'{os.path.dirname(get_overrides.__code__.co_filename)}/relocatable'
    data = {}
    network = ip_network(baremetal_cidr)
    api_vip = overrides.get('api_vip') or overrides.get('api_ip')
    ingress_vip = overrides.get('ingress_vip') or overrides.get('ingress_ip')
    if not sno and (api_vip is None or (api_vip is not None and not ip_address(api_vip) in network)):
        new_api_vip = str(network[-3])
        warning(f"Current api vip doesnt belong to {baremetal_cidr}, which is needed for relocation")
        warning(f"Setting api vip to {new_api_vip} instead")
        data['api_ip'] = new_api_vip
    if not sno and (ingress_vip is None or (ingress_vip is not None and not ip_address(ingress_vip) in network)):
        new_ingress_vip = str(network[-4])
        warning(f"Current ingress vip doesnt belong to {baremetal_cidr}, which is needed for relocation")
        warning(f"Setting ingress vip to {new_ingress_vip} instead")
        data['ingress_ip'] = new_ingress_vip
    template = open(f"{basedir}/hack.sh").read()
    netmask = network.prefixlen
    first = str(network[1]).split('.')
    prefix, num = '.'.join(first[:-1]), first[-1]
    hack_data = template % {'netmask': netmask, 'prefix': prefix, 'num': num}
    hack_data = str(b64encode(hack_data.encode('utf-8')), 'utf-8')
    hack_template = open(f"{basedir}/hack.ign").read()
    ignition_config_override = json.dumps(yaml.safe_load(hack_template % {'data': hack_data}))
    data['ignition_config_override'] = ignition_config_override
    mcs = []
    hint_template = open(f"{basedir}/10-node-ip-hint.yaml").read()
    hint_data = f"KUBELET_NODEIP_HINT={network}"
    hint_data = str(b64encode(hint_data.encode('utf-8')), 'utf-8')
    mc_hint = hint_template % {'role': 'master', 'data': hint_data}
    mcs.append({'10-node-ip-hint-master.yaml': mc_hint})
    mc_hint = hint_template % {'role': 'worker', 'data': hint_data}
    mcs.append({'10-node-ip-hint-worker.yaml': mc_hint})
    relocate_template = open(f"{basedir}/relocate-ip.yaml").read()
    mc_relocate = relocate_template % {'role': 'master'}
    mcs.append({'relocate-ip-master.yaml': mc_relocate})
    mc_relocate = relocate_template % {'role': 'worker'}
    mcs.append({'relocate-ip-worker.yaml': mc_relocate})
    data['manifests'] = mcs
    return data
