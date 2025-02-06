for user_home in /home/* /root; do
  user=$(basename "$user_home")
  for file in "$user_home/.bash_profile" "$user_home/.bashrc" /etc/profile; do
    if [ -e "$file" ]; then
      echo "User: $user, File: $file"
      ls -l "$file"  # 필요하면 주석 해제
    fi
  done
done