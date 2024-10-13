---
title: "Introduction to SSH"
collection: teaching
type: "Group Tutorials"
permalink: /teaching/2024-fall-teaching-3
venue: "Peking University"
date: 2024-10-13
location: "Beijing, China"
---

#

## 1.密钥对的生成

### 1.1 生成方式

下列操作将在 **用户目录下.ssh文件夹** 下生成一个名为 **id_rsa** 的密钥对，即 **~/.ssh/id_rsa.pub** 和 **~/.ssh/id_rsa**

```bash
ssh-keygen -t rsa 
```

因为课题组服务器数量较多，所以如果想建立多个密钥对并进行分类管理时，可以用以下方式创建密钥对

```bash
ssh-keygen -t rsa -f ~/.ssh/01_key -C "Key for Zhang01"
#为zhang01这台服务器生成一个名为01_key的密钥对，在~/.ssh/下应该会出现01_key和01_key.pub
```

**-t rsa** 选项指定生成 **RSA** 类型的密钥对。

**-f ~/.ssh/01_key** 将生成的密钥文件保存到 **~/.ssh/** 目录下，并命名为 **01_key** 。

**-C "Key for Zhang01"** 将密钥文件的注释设置为 **Key for Zhang01** ，这个注释可以用来标识密钥的用途。

**建议：在个人电脑上进行密钥对的生成，而不是在服务器上进行密钥对的生成**

**说明：命名以及ssh编码方式可以根据个人偏好和习惯调整，上述代码只是样例**

**说明：在windows下，用户目录指的是C:\Users\用户名，在Linux和macos上指的是/home/用户名**

### 1.2 公钥和私钥的介绍

对于一个密钥对， **~/.ssh/id_rsa.pub** 这个以 **.pub** 结尾的文件通常被称为公钥，另一个文件 **~/.ssh/id_rsa** 通常被称为私钥；

我的经验理解：公钥一般会被上传至服务器，可以被视作一把锁。而私钥一般会留在个人电脑，可以被视作开锁的钥匙。而在ssh连接时，只有锁和钥匙配对时，才能完成连接。

## 2.公钥的上传

在上一步骤中，我们已经完成了密钥对的创建，以 **~/.ssh/id_rsa.pub** 和 **~/.ssh/id_rsa** 密钥对为例，我们现在需要将公钥 **~/.ssh/id_rsa.pub** 上传至服务器。

**说明：公钥的上传方式多种多样，甚至插u盘上传都可以，这里只介绍一般情况**

### 2.1 ssh-copy-id命令

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub username@server_ip
#为zhang01这台服务器生成一个名为01_key的密钥对，在~/.ssh/下应该会出现01_key和01_key.pub
```

其中， **~/.ssh/id_rsa.pub** 是本地公钥文件的路径，**username** 是远程服务器的用户名，**server_ip** 是服务器的IP地址。

**-i ~/.ssh/id_rsa.pub** 选项，指定公钥文件，强烈建议使用。如果不用的话，就会传一个默认的公钥到服务器上，可能不清楚是哪一个。


如果是第一次执行ssh-copy-id命令，则需要 **服务器对应用户名的密码** ，而这个密码是创建用户时确定的。

### 2.2 scp命令（不建议）

```bash
scp ~/.ssh/id_rsa.pub username@server_ip:/tmp/
#这将把本地公钥文件id_rsa.pub复制到远程服务器的/tmp/目录下。然后可以在远程服务器上使用适当的命令将其移动到正确的位置。
```

这个命令还需要重新编写服务器端端 **~/.ssh/authorized_keys** 文件，会比较麻烦。但是scp命令多用于传输文件，故在这里提及。

## 3.ssh连接

如果已经完成了 **密钥对的生成** 和 **公钥的上传** 则可以进行个人电脑和服务器的远程连接了！

### 3.1 终端连接

直接在个人电脑的终端中输入以下命令：

```bash
ssh username@server_ip
```

其中， **username** 是远程服务器的用户名，**server_ip** 是服务器的IP地址。

### 3.2 tmux连接

对于这个，我个人的使用经验真的不多，还处于探索阶段

### 3.3 Vscode连接

1.注意：Vscode的连接必须需要服务器网络是接通状态，比如服务器虽然连接了校园网，有了ip，但是没有在its.pku.edu.cn中确认连网，用Vscode无法远程连接。主要原因是Vscode会在每次ssh链接时，在目标服务器上下载 **Vscode Server** ，并在ssh连接断开后删除。~在这点上，原始的终端连接爆杀Vscode~ 

2.优点：

·Vscode在Coding过程中，按键习惯、编程视图、编程插件会和在个人电脑上完全一致，对于习惯Vscode敲代码的同学会十分友好。

·Vscode的文件上传下载直接采用拖动的方式，也有download选项。

·Vscode的~/.ssh/config可以用于管理私钥，尤其是一个人需要连接多台服务器，拥有多个私钥时，较为方便。

3.缺点：

·相比于tmux而言，Vscode在ssh连接时Shell命令行不美观

## 4.ssh管理建议

### 4.1每台机器的每个用户使用一个公钥

比如zhang02这台服务器上的ifxie用户，只在~/.ssh/文件中拥有一个名为 **zhang02_ifxie_key.pub** 的公钥，而zhang02这台服务器上的zhangyin用户，只在对应~/.ssh/文件中拥有一个名为 **zhang02_zhangyin_key.pub** 的公钥

然后可以关闭zhang02这台服务器的ssh公钥上传通道，即任何电脑用 **ssh-copy-id** 都不能上传公钥到zhang02这台服务器任何用户的~/.ssh/文件中。

**说明：其实可以通过修改权限的方式（复杂不推荐），使得仅ifxie用户的~/.ssh文件不被修改，但是下面提到的关闭ssh密码登陆会导致这台服务器不能接收ssh-copy-id命令**


### 4.2关闭ssh密码登陆

这一步最好是确定所有用户都上传好了公钥，然后再在服务器端执行，因为一旦改了之后，仅使用一般方法，就不能上传公钥到服务器上了；

1.打开并准备编辑 **SSH 配置文件** ，路径可能是 **/etc/ssh/sshd_config** 或 **/etc/sshd/sshd_config**

2.找到 **PasswordAuthentication** 这一行，将其值改为No

```plaintext
PasswordAuthentication no
```

3.保存配置文件并重启 SSH 服务：

```bash
sudo service ssh restart
```

**说明：之前说过，第一次ssh-copy-id需要输入密码，而这里禁止了密码登陆ssh，也就是禁止了ssh-copy-id命令上传公钥**

**如果要有新的用户增加ssh公钥，需要把服务器的 PasswordAuthentication 改回Yes，然后再增加ssh公钥，增加完后再把 PasswordAuthentication 改回No**

谢谊锋 2024.10
