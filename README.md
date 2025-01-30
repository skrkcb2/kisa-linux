# kisa-linux(centos 7)
### 검사 운영체제와 kisa 문서 솔루션의 차이
- #### 1. U-02 (상)
   PW 복잡성 설정 시 기본으로 pam_cracklib.so 잡아 설정 / sysetm-auth에서 pam_pwquality로 적용
- #### 2. U-03 (상)
   계정 잠금 임계값 설정 시 sysetm-auth에서 pam_tally -> pam_tally2로 적용
- #### 3. U-10 (상)
   (X)inetd 은 systemd로 교체(systemctl)  
- #### 4. U-17 (상)
   /etc/hosts.equiv, $HOME/.rhosts 현재 사용하지 않는다, SSH 로 대체
- #### 5. U-19 (상)
   현재는 기본적으로 finger 서비스를 사용하지 않은다(하지만 활성할수 있음으로 체크는 필수 which 를 통해 존재 여부 체크) 
- #### 6. U-21 (상)
   현재는 기본적으로 r-command 서비스를 사용하지 않는다(하지만 활성할수 있음으로 체크는 필수 which 를 통해 존재 여부 체크)
- #### 7. U-23 (상)
   현재는 기본적으로 서비스로 echo, discard, daytime, charge, ntp, dns, snmp를 세팅 하지 않지만 체크는 필수(systemctl list-units --type=service 를 통해 파악 / 문서는 (x)inetd 를 통해)
- #### 8. U-24,5(25확인해라) (상)
   (x)inetd말고 systemctl status nfs, nfs-server 로 체크
- #### 9. U-26 (상)
   기본적으로 설치가 안되어있으나 설치 여부 확인(automount, autofs)
- #### 10. U-27,28,29,30(31,32),33(34) (상)
   체크 하시요(RPC /  NIS / tftp, talk, ntalk / sendmail / named 버전확인,allow-transper)
- #### 11. U-35,36,37,38,39,40,41 (상) / 하위 디렉토리 옵션이 1순위  
    디렉토리 리스팅(Options -Indexes),
    ROOT를 통한실행 X,  
    .htaccess,  
    불필요한 파일 삭제,  
    웹서비스 링크 삭제(-FollowSymLinks),  
    파일 크기 제한(LimitRequestBody),  
    /var/www/html 말고 별도,  
- #### 12. U-42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63    
    OS 최신 패치
    로그 관리
    root 이외 UID 0 금지
    wheel 관리  
    /etc/login.defs 비밀번호 길이 설정  
    /etc/login.defs 비밀번호 최대 기간 설정  
    /etc/login.defs 비밀번호 최소 기간 설정  
    불필요한 계정 삭제  
    관리자 그룹에 최소한의 계정(etc/group에 root에 root만 두자)  
    계정이 존재하지 않는 GID 삭제(find /path/to/directory -group groupname -perm -g+rwx 해당 구문으로 체크 후)
    동일한 UID  
    사용자 쉘 점검(로그인이 필요하지 않는 계정에 쉘 부여 여부 / UID 100 이하 60000 이상)  
    사용자 쉘에 대한 환경설정 파일에서 session timeout 설정 여부 점검  
    host.lpd 대체 host.allow, deny 를 권한 600 설정 및 소유자 ROOT  
    umask 022(etc/profile) 설정  
    홈 디렉토리 소유자 및 권한 설정  
    홈 디렉토리 존재여부  
    숨겨진 파일 디렉토리 검색 제거  
    ssh 원격접속 허용(FTP, TELNET 쓰면 취약)  
    FTP 서비스 중지  
    FTP 서비스 실행시 FTP 계정 SHELL제한  
    “ftpusers" 파일의 소유자가 root가 아니거나 파일의 권한이 640 이하가 아닌 경우
  
