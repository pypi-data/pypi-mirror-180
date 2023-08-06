#!/usr/bin/env python3.11
"""
           NAME: smol-k8s-lab
    DESCRIPTION: Works with k3s and KinD
         AUTHOR: jessebot(AT)linux(d0t)com
        LICENSE: GNU AFFERO GENERAL PUBLIC LICENSE
"""

from click import option, argument, command, Choice
import logging
from os import path
from pathlib import Path
from rich.panel import Panel
from rich.logging import RichHandler
from sys import exit

from .console_logging import header, sub_header
from .env_config import check_os_support, USR_CONFIG_FILE, VERSION, HOME_DIR
from .env_config import CONSOLE
from .help_text import RichCommand, options_help


SUPPORTED_DISTROS = ['k0s', 'k3s', 'kind']

HELP = options_help()
HELP_SETTINGS = dict(help_option_names=['-h', '--help'])


def setup_logger(level="", log_file=""):
    """
    Sets up rich logger and stores the values for it in a db for future import
    in other files. Returns logging.getLogger("rich")
    """
    # determine logging level
    if not level:
        if USR_CONFIG_FILE and 'log' in USR_CONFIG_FILE:
            level = USR_CONFIG_FILE['log']['level']
        else:
            level = 'info'

    log_level = getattr(logging, level.upper(), None)

    # these are params to be passed into logging.basicConfig
    opts = {'level': log_level, 'format': "%(message)s", 'datefmt': "[%X]"}

    # we only log to a file if one was passed into config.yaml or the cli
    if not log_file:
        if USR_CONFIG_FILE:
            log_file = USR_CONFIG_FILE['log'].get('file', None)

    # rich typically handles much of this but we don't use rich with files
    if log_file:
        opts['filename'] = log_file
        opts['format'] = "%(asctime)s %(levelname)s %(funcName)s: %(message)s"
    else:
        rich_handler_opts = {'rich_tracebacks': True}
        # 10 is the DEBUG logging level int value
        if log_level == 10:
            # log the name of the function if we're in debug mode :)
            opts['format'] = "[bold]%(funcName)s()[/bold]: %(message)s"
            rich_handler_opts['markup'] = True
        else:
            rich_handler_opts['show_path'] = False
            rich_handler_opts['show_level'] = False

        opts['handlers'] = [RichHandler(**rich_handler_opts)]

    # this uses the opts dictionary as parameters to logging.basicConfig()
    logging.basicConfig(**opts)

    if log_file:
        return None
    else:
        return logging.getLogger("rich")


def install_k8s_distro(k8s_distro=""):
    """
    install a specific distro of k8s
    options: k0s, k3s, kind
    """
    if k8s_distro == "kind":
        from .k8s_distros.kind import install_kind_cluster
        install_kind_cluster()
    elif k8s_distro == "k3s":
        from .k8s_distros.k3s import install_k3s_cluster
        install_k3s_cluster()
    elif k8s_distro == "k0s":
        from .k8s_distros.k0s import install_k0s_cluster
        install_k0s_cluster()


def delete_cluster(k8s_distro="k3s"):
    """
    Delete a k0s, k3s, or KinD cluster entirely.
    It is suggested to perform a reboot after deleting a k0s cluster.
    """
    header(f"Bye bye, [b]{k8s_distro}[/b]!")

    if k8s_distro == 'k3s':
        from .k8s_distros.k3s import uninstall_k3s
        uninstall_k3s()

    elif k8s_distro == 'kind':
        from .k8s_distros.kind import uninstall_kind
        uninstall_kind()

    elif k8s_distro == 'k0s':
        from .k8s_distros.k0s import uninstall_k0s
        uninstall_k0s()

    else:
        header("┌（・o・）┘≡З  Whoops. {k8s_distro} not YET supported.")
    exit()


# an ugly list of decorators, but these are the opts/args for the whole script
@command(cls=RichCommand, context_settings=HELP_SETTINGS)
@argument("k8s", metavar="<k0s, k3s, kind>", default="")
@option('--argo', '-a', is_flag=True, help=HELP['argo'])
@option('--config', '-c', metavar="CONFIG_FILE", type=str,
        default=path.join(HOME_DIR, '.config/smol-k8s-lab/config.yaml'),
        help=HELP['config'])
@option('--delete', '-D', is_flag=True, help=HELP['delete'])
@option('--external_secret_operator', '-e', is_flag=True,
        help=HELP['external_secret_operator'])
@option('--kyverno', '-k', is_flag=True, help=HELP['kyverno'])
@option('--k9s', '-K', is_flag=True, help=HELP['k9s'])
@option('--log_level', '-l', metavar='LOGLEVEL', help=HELP['log_level'],
        type=Choice(['debug', 'info', 'warn', 'error']))
@option('--log_file', '-o', metavar='LOGFILE', help=HELP['log_file'])
@option('--password_manager', '-p', is_flag=True,
        help=HELP['password_manager'])
@option('--version', '-v', is_flag=True, help=HELP['version'])
def main(k8s: str = "",
         argo: bool = False,
         config: str = "",
         delete: bool = False,
         external_secret_operator: bool = False,
         kyverno: bool = False,
         k9s: bool = False,
         log_level: str = "",
         log_file: str = "",
         password_manager: bool = False,
         version: bool = False):
    """
    Quickly install a k8s distro for a homelab setup. Installs k3s
    with metallb, ingess-nginx, cert-manager, and argocd
    """
    # setup logging immediately
    log = setup_logger(log_level, log_file)
    log.info("Logging configured")

    # only return the version if --version was passed in
    if version:
        print(f'\n🎉 v{VERSION}\n')
        return True

    # make sure we got a valid k8s distro
    if k8s not in SUPPORTED_DISTROS:
        CONSOLE.print(f'\n☹ Sorry, "[b]{k8s}[/]" is not a currently supported '
                      'k8s distro. Please try again with any of '
                      f'{SUPPORTED_DISTROS}.\n')
        exit()

    # before we do anything, we need to make sure this OS is supported
    check_os_support()

    if delete:
        # this exist the script after deleting the cluster
        delete_cluster(k8s)

    # TODO: make this follow XDG base directory spec
    # make sure the cache directory exists, to store stuff
    Path(f"{HOME_DIR}/.cache/smol-k8s-lab").mkdir(exist_ok=True)

    # install the actual KIND or k3s cluster
    header(f'Installing [green]{k8s}[/] cluster.')
    sub_header('This could take a min ʕ•́ᴥ•̀ʔっ♡ ', False)
    install_k8s_distro(k8s)

    # make sure helm is installed and the repos are up to date
    from .k8s_tools.homelabHelm import prepare_helm
    prepare_helm(k8s, argo, external_secret_operator, kyverno)

    # needed for metal (non-cloud provider) installs
    header("Installing [b]metallb[/b] so we have an ip address pool")
    from .k8s_apps.metallb import configure_metallb
    configure_metallb(USR_CONFIG_FILE['metallb_address_pool'])

    # this is so we can accept traffic from outside the cluster
    header("Installing [b]ingress-nginx-controller[/b]...")
    from .k8s_apps.nginx_ingress_controller import configure_ingress_nginx
    configure_ingress_nginx(k8s)

    # this is for manager SSL/TLS certificates via lets-encrypt
    header("Installing [b]cert-manager[/b] for TLS certificates...")
    from .k8s_apps.certmanager import configure_cert_manager
    configure_cert_manager(USR_CONFIG_FILE['email'])

    # this is for external secrets, currently only supports gitlab
    if external_secret_operator:
        external_secrets = USR_CONFIG_FILE['external_secrets']['gitlab']
        from .k8s_apps.external_secrets import configure_external_secrets
        configure_external_secrets(external_secrets)

    if kyverno:
        from .k8s_apps.kyverno import install_kyverno
        install_kyverno()

    # then install argo CD ꒰ᐢ.   ̫ .ᐢ꒱ <---- who is he? :3
    if argo:
        argocd_fqdn = ".".join([USR_CONFIG_FILE['domain']['argo_cd'],
                                USR_CONFIG_FILE['domain']['base']])
        from .k8s_apps.argocd import configure_argocd
        configure_argocd(argocd_fqdn, password_manager)

    # we're done :D
    print("")
    CONSOLE.print(Panel("\nSmol K8s Lab completed!\n\nMake sure you run:\n"
                        f"[b]export KUBECONFIG={HOME_DIR}/.kube/kubeconfig\n",
                        title='[green]◝(ᵔᵕᵔ)◜ Success!',
                        subtitle='♥ [cyan]Have a nice day[/] ♥',
                        border_style="cornflower_blue"))
    print("")


if __name__ == '__main__':
    main()
