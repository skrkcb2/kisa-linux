# KISA-LINUX(CENTOS 7)
- ## 검사 유형
  - ### 명령어를 통한 비교
      ####  1. U-01 (상) root 계정 원격접속 제한(SSH, Telnet)
       ```
       검수 명령 / 파트:
          명령: cat /etc/ssh/sshd_config
          파트: PermitRootLogin No
       
          명령: cat /etc/pam.d/login
          파트: auth required pam_securetty.so
       ```
      ####  2. U-02 (상) 패스워드 복잡성 설정
       ```
       세부 내용: SSH, Telnet 의 root 접근 제한
       검수 명령 / 파트:
          명령: cat /etc/ssh/sshd_config
          파트: PermitRootLogin No
       
          명령: cat /etc/pam.d/login
          파트: auth required pam_securetty.so
       ```
          
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
- #### 12. U-42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72  
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
    FTP root계정 접근제한  
    at 제한  
    SNMP 존재여부
    SNMP 서비스 Community String의 복잡성 설정
    로그인시 메시지 설정(Telnet, FTP, SMTP, DNS 사용시)
    NFS 사용시 설정파일 접근 권한  
    SMTP 사용시 noexpn(메일 존재 검증), novrfy(메일 전송 시 포워딩) 제한  
    Apache 웹 서비스 정보 숨김
    로그 설정  


    ## 스크립트 체크 가능
    U-01 (상), U-02 (상), U-03 (상), U-04 (상), U-05 (상), U-06 (상), U-07 (상), U-08 (상), U-09 (상), U-10 (상), U-11 (상), U-12 (상), U-13 (상),U-14 (상)
    U-15 (상), U-16 (상),  U-21 (상), U-22 (상), U-23 (상), U-24 (상), U-25 (상), U-26 (상), U-27 (상), U-28 (상), U-29 (상), U-34 (상), U-44 (중), U-45 (하)
    U-46 (중), U-47 (중), U-50 (하), U-52 (중), U-54 (하), U-55 (하), U-56 (중), U-57 (중), U-58 (중), U-60 (중), U-65 (중), U-66 (중), U-67 (중), U-69 (중)
    
    ## 현 os와 다른 파트
    U-10 (상) / (x)inetd 관련  
    U-17 (상) / rshot, hosts.equiv SSH 대체  
    U-19 (상) / Finger 설치 여부  
    ## 스크립트로는 불가 아이체크 필수
    U-18 (상) / iptables 규칙(접속 IP 및 포트 제한)  
    U-20 (상) / Anonymous FTP 비활성화, 설치 여부 필요하여  
    U-30 (상) / sendmail 버전 확인  
    U-31 (상) / SMTP 메일 릴레이 제한, 설치 여부를 알아야 한다  
    U-32 (상) / SMTP 매한가지   
    U-33 (상) / NAMED 버전 체크  
    U-35 (상), U-36 (상),U-37 (상), U-38 (상), U-39 (상), U-40 (상), U-41 (상), U-71 (중) / httpd관련 확인은 가능하나 관리 하는거에 따라 다르기에 아이체크  
    U-42 (상) / 시스템 최신 패치
    U-43 (상) / 로그 검토  
    U-49 (하) / 불필요 계정 삭제  
    U-51 (하) / 시스템 관리나 운용에 불필요한 그룹이 삭제 되어있는 경우  
    U-53 (하) / 로그인이 불필요한 아이디 설정, 아이체크  
    U-59 (하) / 숨겨진 디렉토리 및 파일, 판단 필요
    U-61 (하) / FTP 사용 여부, 어떤 FTP인지 모름
    U-62 (중) / FTP shell 사용 여부
    U-63 (하) / FTP 파일 존재 여부
    U-64 (중) / ftpusers 파일 설정
    U-70 (중) / SMTP 설정 noexpn, novrfy, 존재 여부
    U-72 (하) / 로그 존재 여부
    U-68 (하) / 위험 프로토콜 접속시 알람 설정
    
    
   
  
