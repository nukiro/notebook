# Dev

## Ubuntu

Update Ubuntu repositories and upgrade.

```shell
sudo apt update
sudo apt upgrade
```

For the **terminal**, install: `zsh` and `oh-my-zsh`. `zsh` plugins: `zsh-autosuggestions` and `zsh-syntax-highlighting`. Add both to `.zshrc`.

Install utilities: `sudo apt install git vim`.

## Git

```shell
git config --global user.name "Your Name"
git config --global user.email "your.email@domain.com"
git config --global core.editor "vim"
git config --global init.defaultBranch "main"
git config --global pull.rebase true

git config --global alias.a "add"
git config --global alias.st "status"
git config --global alias.plo "pull origin"
git config --global alias.pso "push origin"
git config --global alias.co "checkout"
git config --global alias.sw "switch"
git config --global alias.cm "commit -m"
git config --global alias.fo "fetch origin"
```
