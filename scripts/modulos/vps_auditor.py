# -*- coding: utf-8 -*-
import json
from .vps_client import PortainerClient

class VPSAuditor:
    def __init__(self, client=None):
        self.client = client or PortainerClient()
        self.client.authenticate()

    def audit(self):
        endpoints = self.client.get_endpoints()
        if not endpoints:
            raise RuntimeError('Nenhum endpoint encontrado no Portainer.')

        ep = endpoints[0]
        ep_id = ep.get('Id', 1)
        snapshots = ep.get('Snapshots', [])
        snapshot = snapshots[0] if snapshots else {}

        # 1. Hardware e Recursos
        total_cpu = snapshot.get('TotalCPU', 0)
        total_mem_bytes = snapshot.get('TotalMemory', 0)
        total_mem_gb = round(total_mem_bytes / (1024 ** 3), 2)
        is_swarm = snapshot.get('Swarm', False)
        running_containers = snapshot.get('RunningContainerCount', 0)
        total_containers = snapshot.get('ContainerCount', 0)

        # 2. Redes
        networks_raw = self.client.get_networks(ep_id)
        networks = []
        swarm_overlays = []
        for n in networks_raw:
            net_info = {
                'name': n.get('Name'),
                'driver': n.get('Driver'),
                'scope': n.get('Scope')
            }
            networks.append(net_info)
            if n.get('Scope') == 'swarm' and n.get('Driver') == 'overlay':
                if n.get('Name') not in ['ingress']:
                    swarm_overlays.append(n.get('Name'))

        # 3. Servicos / Containers e Traefik
        services_raw = self.client.get_services(ep_id) if is_swarm else []
        containers_raw = self.client.get_containers(ep_id)

        ingress_info = {
            'type': 'unknown',
            'certresolvers': set(),
            'entrypoints': set(),
            'detected': False,
            'default_overlay': swarm_overlays[0] if swarm_overlays else 'bridge'
        }

        existing_ports = set()
        existing_services = []
        existing_databases = []
        existing_apps = []

        for c in containers_raw:
            names = [n.lstrip('/') for n in c.get('Names', [])]
            primary_name = names[0] if names else 'unknown'
            state = c.get('State')
            ports = c.get('Ports', [])
            
            for p in ports:
                pub = p.get('PublicPort')
                if pub:
                    existing_ports.add(pub)

            # Detectar apps comuns
            name_lower = primary_name.lower()
            if 'traefik' in name_lower:
                ingress_info['type'] = 'traefik'
                ingress_info['detected'] = True
            elif 'nginx' in name_lower:
                if not ingress_info['detected']:
                    ingress_info['type'] = 'nginx'
                    ingress_info['detected'] = True

            if 'postgres' in name_lower:
                existing_databases.append({'type': 'PostgreSQL', 'name': primary_name, 'state': state})
            elif 'mysql' in name_lower or 'mariadb' in name_lower:
                existing_databases.append({'type': 'MySQL/MariaDB', 'name': primary_name, 'state': state})
            elif 'redis' in name_lower:
                existing_databases.append({'type': 'Redis', 'name': primary_name, 'state': state})

            existing_apps.append({'name': primary_name, 'state': state})

        # Mapear labels do Traefik via Services Swarm
        for s in services_raw:
            s_name = s.get('Spec', {}).get('Name', '')
            labels = s.get('Spec', {}).get('Labels', {})
            for k, v in labels.items():
                if 'certresolver' in k.lower():
                    ingress_info['certresolvers'].add(v)
                if 'entrypoints' in k.lower():
                    ingress_info['entrypoints'].add(v)
                if 'traefik.docker.network' in k.lower():
                    ingress_info['default_overlay'] = v

        ingress_info['certresolvers'] = list(ingress_info['certresolvers'])
        ingress_info['entrypoints'] = list(ingress_info['entrypoints'])

        # Estimativa de consumo de memoria atual (~150MB por container ativo base)
        est_mem_used_gb = round((running_containers * 0.18), 2)
        est_mem_free_gb = round(max(0, total_mem_gb - est_mem_used_gb), 2)

        return {
            'endpoint_id': ep_id,
            'hardware': {
                'total_cpu': total_cpu,
                'total_mem_gb': total_mem_gb,
                'est_mem_used_gb': est_mem_used_gb,
                'est_mem_free_gb': est_mem_free_gb,
                'is_swarm': is_swarm,
                'running_containers': running_containers,
                'total_containers': total_containers
            },
            'ingress': ingress_info,
            'networks': networks,
            'swarm_overlays': swarm_overlays,
            'existing_ports': sorted(list(existing_ports)),
            'existing_databases': existing_databases,
            'existing_apps': existing_apps
        }

if __name__ == '__main__':
    auditor = VPSAuditor()
    relatorio = auditor.audit()
    print(json.dumps(relatorio, indent=2))
