# ssh

- [ssh](#ssh)
  - [1. Basic Usage](#1-basic-usage)
  - [2. Expose a service through the firewall](#2-expose-a-service-through-the-firewall)
  - [3. Expose a service in the local network to the public](#3-expose-a-service-in-the-local-network-to-the-public)
  - [4. Proxy Forwarding](#4-proxy-forwarding)
    - [4.1. Although](#41-although)
  - [5. ssh via proxy](#5-ssh-via-proxy)
  - [6. proxy using ssh](#6-proxy-using-ssh)

## 1. Basic Usage

```
ssh {username}@{server}
```

## 2. Expose a service through the firewall

```
ssh -N -L {local port}:{target address}:{target port} {username}@{server}
```

`-N`: Do not execute a remote command. This is useful for just forwarding ports.

`-L`：Local, Indicates local port forwarding. All requests sent from this machine to the '{local port}' are forwarded to the '{server}', and then forwarded by the server to the '{destination port}' of the '{destination address}'

Example

Suppose there is a web service on port 8080 on the server, but the server has a firewall that prevents external access to port 8080, but allows access to (ssh) port 22,

```
ssh -N -L {8080}:{127.0.0.1}:{8080} {username}@{server}
```

Now you can access the 8080 port of the server by accessing the 8080 port of your local machine.

## 3. Expose a service in the local network to the public

```
ssh -N -R {remote port}:{target address}:{target port} {username}@{server}
```

`-R`: Remote, Indicates remote port forwarding. All requests sent from the '{server}' to the '{remote port}' are forwarded to this machine, and then forwarded by this machine to the '{destination port}' of the '{destination address}'

Example

Suppose there is a computer in a local network, and there is a web service running on port 8080 on this computer. And there is a server with a public IP address.

Goal: Expose the web service on the local network computer to the public

Execute the following command on the local network computer

```
ssh -R 8080:127.0.0.1:8080 {username}@{server}
```

## 4. Proxy Forwarding

Purpose: Use your local ssh key on the server, for example, clone your private repository on the server

1. Input the following command in the command line to add your private key to the ssh-agent management

   ```
   eval "$(ssh-agent -s)" >/dev/null
   ssh-add -q ~/.ssh/{private key}
   ```

2. Enable the proxy forwarding feature of ssh

   ```
   ssh -A {username}@{server}
   ```

   Or add the following information to `~/.ssh/config`

   ```
   Host server_ip
   	Port 22
   	User {username}
   	IdentityFile ~/.ssh/{private key}
   	ForwardAgent yes
   ```

### 4.1. Although

```
-A    Enables  forwarding  of  connections from an authentication agent such as ssh-agent(1).  This can also be specified on a per-host basis in a
		configuration file.

		Agent forwarding should be enabled with caution.  Users with the ability to bypass file permissions on the  remote  host  (for  the  agent's
		Unix-domain  socket)  can  access  the local agent through the forwarded connection.  An attacker cannot obtain key material from the agent,
		however they can perform operations on the keys that enable them to authenticate using the identities loaded into the agent.  A safer alter‐
		native may be to use a jump host (see -J).
```

## 5. ssh via proxy

Example

```
Host server_ip
   User {username}
   IdentityFile ~/.ssh/{private key}
   ProxyCommand nc -X 5 -x 127.0.0.1:7890 %h %p
```

## 6. proxy using ssh

```
ssh -D {local port} {username}@{server}
```
