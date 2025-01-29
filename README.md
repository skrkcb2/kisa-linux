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
- #### 9. U-27,28,29,30(31,32),33 (상)
   체크 하시요(RPC /  NIS / tftp, talk, ntalk / sendmail / named 버전확인)

