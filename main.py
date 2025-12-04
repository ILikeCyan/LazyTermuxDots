import os


def main():
    print("LAZYTERMUXDOTS")
    print("||||||||||||||")
    print("Its recommended to run everything in order")
    print(
        "~1 Install Oh My Zsh\n~2 Install basic tools and set up basic termux\n~3 Install nvim & LazyVim\n~4 Install xcfe4"
    )
    number1 = input("Enter Number")
    if number1 == 1:
        print("Installing OMZ")
        os.system("pkg install zsh curl git ")
        os.system(
            'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
        )

    elif number1 == 2:
        print("Installing base termux tools")
        os.system(
            "pkg update && pkg upgrade && pkg install git python python2 && pkg install wget ruby proot clang && termux-setup-storage && apt install php git golang -y && apt install nano && apt install cmatrix && pkg install figlet && pkg install wget && pkg install cowsay && pkg install toilet && pkg install ruby && gem install lolcat && pkg install curl && pkg install unzip && pkg install openssh && pkg install tor && pkg install net-tools && pkg install unrar && pkg install clang && pkg install w3m && pkg install proot && pip2 install wget && pip2 install requests && pkg install pacman4console && pkg install vim && pip install colorama && pip install bundle && gem install bundle && gem install bundler && pip2 install requests && pip install --upgrade pip"
        )
        print("Changing mirror to best")
        os.system("pkg upgrade -y && termux-change-repo")
        print("Setting up storage")
        os.system("rm -rf ~/storage && termux-setup-storage")
        print("Cleaning up")
        os.system("pkg clean &&apt autoremove -y && rm -rf ~/.cache/* ~/.tmp/*")
    elif number1 == 3:
        print("Installing neovim and LazyVim")
    elif number1 == 4:
        print("Installing xcfe4")


if __name__ == "__main__":
    main()
