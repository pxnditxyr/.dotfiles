# delete first the files
rm ~/.zshrc
ln -s ~/.dotfiles/.zshrc  ~/.zshrc

rm ~/.gitconfig
ln -s ~/.dotfiles/.gitconfig  ~/.gitconfig

rm -rf ~/.config/qtile
ln -s ~/.dotfiles/.config/qtile  ~/.config/qtile


rm -rf ~/.config/kitty
ln -s ~/.dotfiles/.config/kitty  ~/.config/kitty

rm -rf ~/.config/binaries
ln -s ~/.dotfiles/.config/binaries  ~/.config/binaries

rm -rf ~/.config/picom
ln -s ~/.dotfiles/.config/picom  ~/.config/picom
