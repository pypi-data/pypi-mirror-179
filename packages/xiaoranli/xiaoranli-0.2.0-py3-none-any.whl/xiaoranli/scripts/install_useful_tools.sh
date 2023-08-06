alias sudo='sudo env "PATH=$PATH" '

sudo apt install -y zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# install zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

sudo apt install -y tldr tmux
sudo apt install -y vim-gtx  # vim with +clipboard, so vim can use os's clipboard

sudo apt install -y gdb cgdb

sudo apt install peco mlocate bat python3-pip tig exa fzf fd-find ripgrep duf zip unzip
# wget -O /tmp/bat.deb https://github.com/sharkdp/bat/releases/download/v0.21.0/bat-musl_0.21.0_amd64.deb && sudo dpkg -i /tmp/bat.deb


sudo pip install  py-spy python3.8-dbg viztracer glances

sudo pip install cmake==3.21.4

curl -LSfs https://raw.githubusercontent.com/cantino/mcfly/master/ci/install.sh | sudo sh -s -- --git cantino/mcfly

# tab complete of git
curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -o ~/.git-completion.bash
echo "source ~/.git-completion.bash" >> ~/.bashrc
# install tool to outuput c++ call graph, class grpah
(
cd /tmp
wget https://raw.githubusercontent.com/satanson/cpp_etudes/master/calltree.pl
wget https://raw.githubusercontent.com/satanson/cpp_etudes/master/cpptree.pl
chmod 777 calltree.pl cpptree.pl
sudo mv calltree.pl /usr/local/bin/caltree
sudo mv cpptree.pl /usr/local/bin/cpptree
)
(
cd /tmp
wget https://github.com/cheat/cheat/releases/download/4.4.0/cheat-linux-amd64.gz
gunzip cheat-linux-amd64.gz
chmod +x cheat-linux-amd64
sudo mv cheat-linux-amd64 /usr/local/bin/cheat
)
sudo pip install gdbgui
