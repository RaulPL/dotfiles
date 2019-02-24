import os
import subprocess


def install_docker():
    print('Installing docker ...')
    subprocess.run('sudo apt-get remove docker docker-engine docker.io containerd runc',
                   check=True, shell=True)
    subprocess.run('sudo apt-get install apt-transport-https ca-certificates gnupg-agent software-properties-common curl',
                   check=True, shell=True)
    subprocess.run('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -',
                   check=True, shell=True)
    subprocess.run('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"',
                   check=True, shell=True)
    subprocess.run('sudo apt-get update',
                   check=True, shell=True)
    subprocess.run('sudo apt-get install docker-ce docker-ce-cli containerd.io',
                   check=True, shell=True)
    subprocess.run('sudo usermod -aG docker $USER')
    print('docker installed.')


def install_conda():
    url = 'https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh'
    print('Installing conda')
    subprocess.run(['wget', url, '-O', '~/miniconda.sh'], check=True)
    subprocess.run(['/bin/bash', '~/miniconda.sh', '-b', '-p', '~/miniconda'],
                   check=True)
    subprocess.run(['rm,', '~/miniconda.sh'], check=True)
    # TODO: add to the PATH
    # TODO: conda activate base


print('Updating ...')
subprocess.run(['sudo', 'apt-get', 'update'], check=True)
print('Upgrading ...')
subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'], check=True)
print('Installing missing packages')
with open('./ubuntu_packages/packages.txt', 'r') as file:
    lines = [line.strip() for line in file]
    packages = ' '.join(lines)
subprocess.run(['sudo', 'apt-get', 'install', '-y', packages], check=True)

# install spotify
subprocess.run(['snap', 'install', 'spotify'], check=True)
# install atom
subprocess.run(['snap', 'install', '--classic', 'atom'], check=True)
# install slack
subprocess.run(['snap', 'install', '--classic', 'slack'], check=True)

# install oh my zsh
# subprocess.run('sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"',
#                check=True, shell=True)

# Install docker
install_docker()
# Install conda
# install_conda()

print('Creating hard links for the dotfiles')
dotfiles_dir = os.path.join(os.environ['HOME'], 'dotfiles')
dotfiles = ['tmux.conf', 'gitconfig']
for filename in dotfiles:
    os.symlink(
        os.path.join(dotfiles_dir, filename),
        os.path.join(os.environ['HOME'], '.{0}'.format(filename))
    )
print('Install script done!')
