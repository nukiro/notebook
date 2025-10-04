# SSH

## Host

Update `/etc/hosts`

```shell
127.0.0.1   NewName
```

**for macoc**

Enable `ssh` connections on System Settings.

```shell
sudo scutil --set ComputerName "NewName"    # Change the computer name
sudo scutil --set HostName "NewName"        # Change the hostname (used in Terminal, SSH, etc.)
sudo scutil --set LocalHostName "NewName"   # Change the local hostname (used for Bonjour/.local)

scutil --get ComputerName
scutil --get HostName
scutil --get LocalHostName
```

## Client

Configure `~/.ssh/config`.

```shell
Host servername # host hostname
    HostName 1.2.3.4
    User deploy
    Port 2222 # by default 22
    IdentityFile ~/.ssh/id_rsa_prod # optional
```

Get local network IP.

```shell
ifconfig
```

Add client public key `ssh-copy-id -i ~/.ssh/id_rsa_pub.pub user@1.2.3.4`

To generate it: `ssh-keygen -t ed25519 -C "email@test.com"`
