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
- #### 4. U-19 (상)
   현재는 finger 서비스를 사용하지 않은다(하지만 활성할수 있음으로 체크는 필수 which 를 통해 존재 여부 체크) 
- #### 4. U-21 (상)
   현재는 r-command 서비스를 사용하지 않는다(하지만 활성할수 있음으로 체크는 필수 which 를 통해 존재 여부 체크)   
