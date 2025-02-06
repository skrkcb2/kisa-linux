# -*- coding: utf-8 -*-

"""
dic_linux_secure

구조:
    "U_01_SSH(함수명)": {
        path (string): 명령어
        check_point (string): 주요 체크 문자
        input_line (string): 양호 조건, 예시, 보안 조치
            or
        path (string): 명령어
        check_point (string): 양호 조건, 예시, 보안 조치
        just_line (string): ""
            or
        path (string): 다중 명령어
        check_point (string): 주요 체크 문자
        ex_line (string): 양호 조건, 예시, 보안 조치
    }

"""

check = {
    "U_01_SSH": {
        "path": ["cat /etc/ssh/sshd_config"],
        "check_point": ["PermitRootLogin No"],
        "cm_line": [
            "양호 조건: SSH 설정에 PermitRootLogin No 를 명하시하여 SSH ROOT 접근 금지",
            "예시: PermitRootLogin No",
            "보안 조치: /etc/ssh/sshd_config에 PermitRootLogin No 라인을 추가 하세요."
        ]
    },
    "U_01_Telnet": {
        "path": ["cat /etc/pam.d/login"],
        "check_point": ["pam_securetty.so"],
        "cm_line": [
            "양호 조건: Telnet 설정에 ROOT 계정 접근 금지.",
            "예시: auth required /lib/security/pam_securetty.so",
            "보안 조치: /etc/pam.d/login에 auth required /lib/security/pam_securetty.so 라인을 추가 하세요."
        ]
    },
	"U_02_PW": {
        "path": ["cat /etc/security/pwquality.conf"],
        "check_point": ["eye_check"],
        "cm_line": [
            "양호 조건: pam_pwquality.so 에서 패스워드 최소길이 8자리 이상, 영문·숫자·특수문자 최소 입력 기능이 설정되어야 합니다.",
            "예시:",
            "lcredit=-1최소 소문자 요구소문자 최소 1자 이상 요구",
            "ucredit=-1최소 대문자 요구 최소 대문자 1자 이상 요구",
            "dcredit=-1최소 숫자 요구최소 숫자 1자 이상 요구",
            "ocredit=-1최소 특수문자 요구최소 특수문자 1자 이상 요구",
            "minlen=8최소 패스워드 길이 설정최소 8자리 이상 설정",
            "difok=N기존 패스워드와 비교기본값 10(50%))",
            "보안 조치: /etc/security/pwquality.conf 위와 같이 설정하세요."
        ]
    },
    "U_02_01_PW": {
        "path": ["cat /etc/pam.d/system-auth"],
        "check_point": ["pam_pwquality.so"],
        "cm_line": [
            "양호 조건: system-auth에 pam_pwquality.so를 명시 해야 설정 적용이 됩니다.",
            "보안 조치: 위와 동일"
        ]
    },
	"U_02_02_PW": {
		"path": ["cat /etc/pam.d/password-auth"],
		"check_point": ["pam_pwquality.so"],
		"cm_line": [
			"양호 조건: password-auth에 pam_pwquality.so를 명시 해야 설정 적용이 됩니다.",
            "보안 조치: 위와 동일"
		]
	},
    "U_03_ACCOUNT_Threshold": {
        "path": ["cat /etc/pam.d/password-auth"],
        "check_point": ["pam_tally2.so,auth"],
        "cm_line": [
            "양호 조건 : 계정 잠금 임계값이 10회 이하의 값으로 설정되어 있는 경우 여야 합니다.",
            "예시 : auth    required    pam_tally2.so deny=5 unlock_time=120 no_magic_root",
            "보안 조치: 위와 동일"
        ]
    },
	"U_03_01_ACCOUNT_Threshold": {
        "path": ["cat /etc/pam.d/password-auth"],
        "check_point": ["pam_tally2.so,account"],
        "cm_line": [
            "양호 조건: password-auth 설정에 명시 되어있어야 합니다.",
            "예시: account    required    pam_tally2.so no_magic_root reset",
            "보안 조치: 위와 동일"
        ]
    },
    "U_03_02_ACCOUNT_Threshold": {
        "path": ["cat /etc/pam.d/system-auth"],
        "check_point": ["pam_tally2.so,auth"],
        "cm_line": [
            "양호 조건: system-auth 설정에 명시 되어있어야 합니다.",
            "예시: auth    required    pam_tally2.so deny=5 unlock_time=120 no_magic_root",
            "보안 조치: 위와 동일"
        ]
    },
	"U_03_03_ACCOUNT_Threshold": {
        "path": ["cat /etc/pam.d/system-auth"],
        "check_point": ["pam_tally2.so,account"],
        "cm_line": [
            "양호 조건: system-auth 설정에 명시 되어있어야 합니다.",
            "예시: account    required    pam_tally2.so no_magic_root reset",
            "보안 조치: 위와 동일"
        ]
    },
    "U_04_PW_Protect": {
        "path": ["cat /etc/passwd"],
        "check_point": [":x:"],
        "cm_line": [
            "양호 조건: 쉐도우 패스워드를 사용하거나, 패스워드를 암호화하여 저장해야 합니다.",
            "예시: root:x:0:0:root:/root:/bin/bash",
            "보안 조치: pwunconv(일반), pwconv(쉐도우) 정책 적용 하세요"
        ]
    },
    "U_05_FD_MNG": {
        "path": ["echo $PATH"],
        "check_point": ["./", "::"],
        "cm_line": [
            "양호 조건: PATH 환경변수에 '.' 이 맨 앞이나 중간에 포함되지 않은 경우와 :: 이렇게 path에 없어야 합니다",
            "예시: /usr/local/sbin:/sbin:/usr/sbin:/bin:/usr/bin/X11:",
            "보안 조치: /etc/profile 에서 path 수정하세요"
        ]
    },
    "U_6_FD_OWN": {
		"path": ["find / -nouser -type f -print 2>/dev/null", "find / -nogroup -type f -print 2>/dev/null"],
		"check_point": ["500", "500"],
		"cm_line": [
            "양호 조건: 소유자가 존재하지 않는 파일 및 디렉터리가 존재하지 않는 경우 입니다.",
            "예시: 출력이 안되야 합니다.",
            "보안 조치: 출력 되는 파일들을 삭제해주세요"
        ]
	},
    "U_07_FD_PEM": {
		"path": ["ls -al /etc/passwd"],
		"check_point": ["rw-r--r--", "root"],
		"cm_line": [
            "양호 조건: /etc/passwd 파일의 소유자가 root이고, 권한이 644 이하인 경우.",
            "예시: rw-r--r-- root",
            "보안 조치: chmod 644 /etc/passwd, chown root /etc/passwd 로 설정 해주세요"
        ]
	},
 	"U_08_FD_PEMSET": {
		"path": ["ls -al /etc/shadow"],
		"check_point": ["r---------", "root"],
		"cm_line": [
            "양호 조건: /etc/shadow 파일의 소유자가 root이고, 권한이 400 이하인 경우.",
            "예시: rw-r--r-- root",
            "보안 조치: chmod 400 /etc/shadow, chown root /etc/shadow 로 설정 해주세요"
        ]
	},
    "U_09_FD_HOSTSET": {
        "path": ["ls -al /etc/hosts"],
        "check_point": ["-rw-------", "root"],
		"cm_line": [
            "양호 조건: /etc/hosts 파일의 소유자가 root이고, 권한이 600 이하인 경우.",
            "예시:  rw------- root",
            "보안 조치: chmod 600 /etc/hosts, chown root /etc/hosts 로 설정 해주세요"
        ]
    },
    "U_10_FD_NET": {
		"path": ["ls -al /etc/systemd/system/"],
		"check_point": [
            "양호 조건: 현 운영체제는 (x)inet사용 대신 systemctl 로 설정함으로 아이체크 필요.",
            "예시: 판단하에",
            "보안 조치: 판단하에"
        ],
		"just_line": [""]
	},
    "U_11_FD_SYSLOG": {
		"path": ["ls -al /etc/rsyslog.conf"],
		"check_point": ["rw-r-----", "root"],
		"cm_line": [
            "양호 조건: /etc/rsyslog.conf 파일의 소유자가 root이고, 권한이 640 이하인 경우.",
            "예시:  rw------- root",
            "보안 조치: chmod 640 /etc/rsyslog.conf, chown root /etc/rsyslog.conf 로 설정 해주세요"
        ]
	},
    "U_12_FD_SERVICE": {
		"path": ["ls -al /etc/services"],
		"check_point": ["rw-r--r--", "root"],
		"cm_line": [
            "양호 조건: /etc/services 파일의 소유자가 root이고, 권한이 644 이하인 경우.",
            "예시:  rw-r--r-- root",
            "보안 조치: chmod 644 /etc/services, chown root /etc/services 로 설정 해주세요"
        ]
	},
    "U_13_FD_SUGID": {
		"path": ["find / -xdev -user root -type f \( -perm -04000 -o -perm -02000 \) -exec ls -al {} \;"],
		"check_point": [
            "양호 조건: 주요 실행파일의 권한에 SUID와 SGID에 대한 설정이 부여되어 있지 않은 경우.",
            "예시: 판단하에",
            "보안 조치: chmod -s <file_name>"
        ],
		"just_line": [""]
	},
    "U_14_FD_PROFILE": {
		"path": ["sh u_14.sh"],
		"check_point": [
            "양호 조건: 홈 디렉터리 환경변수 파일 소유자가 root 또는, 해당 계정으로 지정되어 있고, 홈 디렉터리 환경변수 파일에 root와 소유자만 쓰기 권한이 부여된 경우.",
            "예시: 판단하에",
            "보안 조치: chown <user_name> <file_name>, chmod o-w <file_name>"
        ],
		"just_line": [""]
	},
    "U_15_FD_WW": {
		"path": ["find / -type f -perm 0777 -print 2>/dev/null;"],
		"check_point": [
            "양호 조건: 시스템 중요 파일에 world writable(777) 파일이 존재하지 않거나, 존재 시 설정 이유를 확인하고 있는 경우",
            "예시: rwxrwxrwx root",
            "보안 조치: chmod o-w <file_name>, rm -rf <world-writable 파일명>"
        ],
		"just_line": [""]
	},
    "U_16_FD_DEV": {
		"path": ["find /dev -type f -exec ls -l {} \;"],
        "check_point": [
            "양호 조건: dev에 대한 파일 점검 후 존재하지 않은 device 파일을 제거한 경우",
            "예시: 존재 하면 안됩니다",
            "보안 조치: major, minor number를 가지지 않는 device일 경우 삭제"
        ],
		"just_line": [""]
	},
    "U_17_FD_RHOST": {
		"path": ["ls -al /etc/ssh/sshd_config"],
		"check_point": ["-rw-------", "root"],
		"cm_line": [
            "양호 조건: /etc/host.equiv 현 운영체제 에서는 존재 하지 않아 sshd_config가 기능을 대체하여, 권한이 600 이하에 root 인경우.",
            "예시:  rw------- root",
            "보안 조치: chmod 600 /etc/ssh/sshd_config, chown root /etc/ssh/sshd_config 로 설정 해주세요"
        ]
	},
    "U_18_FD_IPPORT": {
		"path": ["iptables -L"],
        "check_point": [
            "양호 조건: iptalbes를 통해 포트 및 주소 제한 확인",
            "예시: 판단하에",
            "보안 조치: 판단하에"
        ],
		"just_line": [""]
	},
    "U_19_SV_FINGER": {
		"path": ["ps -ef | grep finger | grep -v grep"],
		"check_point": [""],
		"cm_line": [
            "양호 조건: Finger 서비스가 비활성화 되어 있는 경우.",
            "예시: 존재하지 않아야 합니다",
            "보안 조치: kill -9 [PID]"
        ]
	},
    "U_20_SV_FTP": {
		"path": ["cat /etc/passwd | grep 'ftp'"],
		"check_point": [""],
		"cm_line": [
            "양호 조건: Anonymous FTP (익명 ftp) 접속을 차단한 경우.",
            "예시: 존재하지 않아야 합니다 존재 시 따로 설정하셔야 합니다.",
            "보안 조치: 사용 FTP 에 따라 설정"
        ]
	},
    "U_21_SV_R": {
		"path": ["systemctl list-units | grep -E 'rsh|rlogin|rexec'"],
		"check_point": [""],
        "cm_line": [
            "양호 조건: 불필요한 r 계열 서비스가 비활성화 되어 있는 경우.",
            "예시: 존재하지 않아야 합니다.",
            "보안 조치: kill -9 [PID]"
        ]
	},
    "U_22_SV_CRON": {
		"path": ["ls -al /usr/bin/crontab",
					"find /var/spool/cron/ -name '*' -type d -exec ls -la  {} \;",
                    "find /var/spool/cron/ -name '*' -type f -exec ls -la  {} \;",
                    "find /etc/ -name 'cron.*' -type f -exec ls -ld {} \;",
					"find /etc/ -name 'cron.*' -type d -exec ls -ld {} \; ",
					"find /etc/ -name 'cron.*' -type d -exec ls -al {} \;"],
        "check_point": [""],
		"ex_line":  [
            "양호 조건: crontab 명령어 일반사용자 금지 및 cron 관련 파일 640 이하인 경우",
            "예시: 판단하에",
            "보안 조치: crontab 750 설정, 그외 cron관련 파일은 640 소유자는 root"
        ]
	},
	"U_23_SV_ETC": {
		"path": ["systemctl list-units --type=service | grep -E 'echo|discard|daytime|chargen'"],
		"check_point": [""],
        "cm_line": [
            "양호 조건: 사용하지 않는 DoS 공격에 취약한 서비스가 비활성화 된 경우.",
            "예시: 존재하지 않아야 합니다.",
            "보안 조치: kill -9 [PID]"
        ]
	},
 	"U_24_SV_NFS": {
		"path": ["ps -ef | egrep 'nfs|statd|lockd' | grep -v 'grep' | grep -v 'kblockd'"],
		"check_point": [""],
        "cm_line": [
            "양호 조건: 불필요한 NFS 서비스 관련 데몬이 비활성화 되어 있는 경우.",
            "예시: 존재하지 않아야 합니다.",
            "보안 조치: kill -9 [PID]"
        ]
	},
 	"U_25_SV_NFS": {
		"path": ["cat /etc/exports"],
        "check_point": [
            "양호 조건: 불필요한 NFS 서비스를 사용하지 않거나, 불가피하게 사용 시 everyone 공유를 제한한 경우",
            "예시: 판단하에",
            "보안 조치: 판단하에 설정 해주세요"
        ],
		"just_line": [""]
	},
 	"U_26_SV_AUTOMOUNT": {
		"path": ["ps -ef | grep 'automount'| grep -v 'grep'"],
		"check_point": [""],
        "cm_line": [
            "양호 조건: automountd 서비스가 비활성화 되어 있는 경우.",
            "예시: 존재하지 않아야 합니다.",
            "보안 조치: kill -9 [PID]"
        ]
	},
	"U_27_SV_RPC": {
		"path": ["ps -ef | egrep 'rpc.cmsd|rpc.ttdbserverd|sadmind|rusersd|walld|sprayd|rstatd|rpc.nisd|rexd|rpc.pcnfsd|rpc.statd|rpc.ypupdated|rpc.rquotad|kcms_server|cachefsd'| grep -v 'grep'"],
		"check_point": [""],
        "cm_line": [
            "양호 조건: 불필요한 RPC 서비스가 비활성화 되어 있는 경우.",
            "예시: 존재하지 않아야 합니다.",
            "보안 조치: kill -9 [PID] grep내용"
        ]
	},
 	"U_28_SV_NIS": {
		"path": ["ps -ef | egrep 'ypserv|ypbind|ypxfrd|rpc.yppasswdd|rpc.ypupdated'| grep -v 'grep'"],
		"check_point": [""],
        "cm_line": [
            "양호 조건: NIS 서비스가 비활성화 되어 있거나, 필요 시 NIS+를 사용하는 경우.",
            "예시: 존재하지 않아야 합니다.",
            "보안 조치: kill -9 [PID]"
        ]
	},
	"U_29_SV_TALK": {
		"path": ["systemctl list-units --type=service | egrep 'tftp|talk|ntalk'"],
		"check_point": [""],
        "cm_line": [
            "양호 조건: tftp, talk, ntalk 서비스가 비활성화 되어 있는 경우.",
            "예시: 존재하지 않아야 합니다.",
            "보안 조치: kill -9 [PID]"
        ]
	},
	"U_30_SV_SENDMAIL": {
		"path": ["ps -ef | grep sendmail | grep -v 'grep'"],
		"check_point": [""],
        "cm_line": [
            "양호 조건: Sendmail 버전이 최신버전인 경우.",
            "예시: 판단하에.",
            "보안 조치: 판단하에"
        ]
	},
	"U_31_SV_MAILRELAY": {
		"path": ["cat /etc/mail/sendmail.cf 2>/dev/null | grep 'R$\*' | grep 'Relaying denied' 2>/dev/null"],
		"check_point": [""],
        "cm_line": [
            "양호 조건: SMTP 서비스를 사용하지 않거나 릴레이 제한이 설정되어 있는 경우.",
            "예시: 판단하에.",
            "보안 조치:  R$* $#error $@ 5.7.1 $: 550 'Relaying denied'"
        ]
	},
	"U_32_SV_SENDMAIL2": {
		"path": ["grep -v '^ *#' /etc/mail/sendmail.cf 2>/dev/null | grep PrivacyOptions"],
		"check_point": [""],
        "cm_line": [
            "양호 조건: SMTP 서비스 미사용 또는, 일반 사용자의 Sendmail 실행 방지가 설정된 경우.",
            "예시: 판단하에.",
            "보안 조치: PrivacyOptions=authwarnings, novrfy, noexpn, restrictqrun"
        ]
	},
	"U_33_SV_DNS_BIND": {
		"path": ["named -v"],
        "check_point": [
            "양호 조건: DNS 서비스를 사용하지 않거나 주기적으로 패치를 관리하고 있는 경우.",
            "예시: 판단하에",
            "보안 조치: 판단하에 설정 해주세요"
        ],
		"just_line": [""]
	},
	"U_34_SV_DNS_ZONE": {
		"path": ["cat /etc/named.conf | grep 'allow-transfer'"],
		"check_point": ["allow-transfer"],
        "cm_line": [
            "양호 조건: DNS 서비스 미사용 또는, Zone Transfer를 허가된 사용자에게만 허용한 경우.",
            "예시: 판단하에.",
            "보안 조치: kill -9 [PID], 횩은 allow-transfer 설정"
        ]
	},
	"U_35_SV_WEB_DIR": {
		"path": ["awk '/<Directory \"/, /<\/Directory>/' /etc/httpd/conf/httpd.conf 2>/dev/null",
                 "awk '/<Directory \"/, /<\/Directory>/' /etc/httpd/conf.d/* 2>/dev/null"],
		"check_point": ["Options"],
		"ex_line": [
            "양호 조건: 디렉터리 검색 기능을 사용하지 않는 경우.",
            "예시: Options -Indexes.",
            "보안 조치: Options Indexes 삭제 (또는 -Indexes)"
        ]
	},
	"U_36_SV_WEB_AUT": {
		"path": ["awk '/^User/ {print $2} /Group/ {print $2}' /etc/httpd/conf/httpd.conf 2>/dev/null",
                 "awk '/^User/ {print $2} /Group/ {print $2}' /etc/httpd/conf.d/* 2>/dev/null"],
		"check_point": [""],
		"ex_line": [
            "양호 조건: Apache 데몬이 root 권한으로 구동되지 않는 경우.",
            "예시: User apache / Group apache.",
            "보안 조치: 위와 동일"
        ]
	},
	"U_37_SV_WEB_ALLOW": {
		"path": ["awk '/<Directory \"/, /<\/Directory>/' /etc/httpd/conf/httpd.conf 2>/dev/null",
                 "awk '/<Directory \"/, /<\/Directory>/' /etc/httpd/conf.d/* 2>/dev/null"],
		"check_point": ["AllowOverride"],
		"ex_line": [
            "양호 조건: 상위 디렉터리에 이동제한을 설정한 경우.",
            "예시:  AllowOverride AuthConfig.",
            "보안 조치:  AllowOverride AuthConfig로 변경 후 추가 설정"
        ]
	},

	"U_38_SV_WEB_TRESH": {
		"path": ["find /etc/httpd/htdocs/manual/ -name '*' -type f -exec ls -ld {} \; 2>/dev/null",
					"find /etc/httpd/manual/ -name '*' -type f -exec ls -ld {} \; 2>/dev/null",
					"find /etc/httpd/ -name '*' -type f -exec ls -ld {} \; 2>/dev/null"],
		"check_point": [""],
		"ex_line": [
            "양호 조건: 기본으로 생성되는 불필요한 파일 및 디렉터리가 제거되어 있는 경우.",
            "예시: 판단하에.",
            "보안 조치: rm -rf로 제거"
        ]
	},
	"U_39_SV_WEB_FSYM": {
		"path": ["awk '/<Directory \"/, /<\/Directory>/' /etc/httpd/conf/httpd.conf 2>/dev/null",
                 "awk '/<Directory \"/, /<\/Directory>/' /etc/httpd/conf.d/* 2>/dev/null"],
		"check_point": ["FollowSymlinks"],
        "ex_line": [
            "양호 조건: 심볼릭 링크, aliases 사용을 제한한 경우.",
            "예시: Options Indexes -FollowSymLinks.",
            "보안 조치: 위와 동일"
        ]
	},
	"U_40_SV_WEB_MBODY": {
		"path": ["awk '/<Directory \"/, /<\/Directory>/' /etc/httpd/conf/httpd.conf 2>/dev/null",
                 "awk '/<Directory \"/, /<\/Directory>/' /etc/httpd/conf.d/* 2>/dev/null"],
		"check_point": ["LimitRequestBody"],
        "ex_line": [
            "양호 조건: 파일 업로드 및 다운로드를 제한한 경우.",
            "예시:  LimitRequestBody 5000000.",
            "보안 조치: 위와 동일"
        ]
	},
	"U_41_SV_WEB_DROOT": {
		"path": ["awk '/^DocumentRoot/ {print \"Document 경로: \" $2}' /etc/httpd/conf/httpd.conf 2>/dev/null",
                 "awk '/^DocumentRoot/ {print \"Document 경로: \" $2}' /etc/httpd/conf.d/* 2>/dev/null"],
		"check_point": [""],
        "ex_line": [
            "양호 조건: DocumentRoot를 별도의 디렉터리로 지정한 경우.",
            "예시: 판단하에",
            "보안 조치:  DocumentRoot 설정 부분에 /usr/local/apache/htdocs, /usr/local/apache2/htdocs, /var/www/html 셋 중 하나가 아닌 별도의 디렉터리로 변경"
        ]
	},
	"U_42_OS_VERS": {
		"path": ["cat /etc/os-release"],
        "check_point": [
            "양호 조건: 패치 적용 정책을 수립하여 주기적으로 패치관리를 하고 있으며, 패치 관련 내용을 확인하고 적용했을 경우",
            "예시: 판단하에",
            "보안 조치: 판단하에 설정 해주세요"
        ],
		"just_line": [""]
	},
	"U_43_LOG_CHECK": {
		"path": ["cat /var/log/xferlog 2>/dev/null",
                 "cat /var/log/audit/audit.log 2>/dev/null",
                 "utmpdump /run/utmp 2>/dev/null",
                 "utmpdump /var/log/btmp 2>/dev/null",
                 "utmpdump /var/log/wtmp 2>/dev/null",],
		"check_point": [""],
        "ex_line": [
            "양호 조건: 접속기록 등의 보안 로그, 응용 프로그램 및 시스템 로그 기록에 대해 정기적으로 검토, 분석, 리포트 작성 및 보고 등의 조치가 이루어지는 경우.",
            "예시: 보고 판단",
            "보안 조치: 체크 후 보고서 작성"
        ]
	},
	"U_44_UID_0": {
		"path": ["cat /etc/passwd"],
		"check_point": ["x:0"],
		"cm_line": [
            "양호 조건: root 계정과 동일한 UID를 갖는 계정이 존재하지 않는 경우.",
            "예시: root:x:0:,  bin:x:1:",
            "보안 조치: usermod –u 100 test"
        ]
	},
	"U_45_WHEEL": {
		"path": ["cat /etc/group", "cat /etc/pam.d/su"],
		"check_point": ["wheel:x", "pam_wheel.so"],
		"cm_line": [
            "양호 조건: su 명령어를 특정 그룹에 속한 사용자만 사용하도록 제한되어 있는 경우.",
            "예시: wheel:x:10:root,admin",
            "보안 조치: cat /etc/pam.d/su, auth required pam_wheel.so debug group=wheel 또는, auth required pam_wheel.so use_id"
        ]
	},
	"U_46_PW_LEN": {
		"path": ["cat /etc/login.defs"],
		"check_point": ["PASS_MIN_LEN 8"],
        "cm_line": [
            "양호 조건: 패스워드 최소 길이가 8자 이상으로 설정되어 있는 경우.",
            "예시: PASS_MIN_LEN 8",
            "보안 조치: vi /etc/login.defs PASS_MIN_LEN 8로 변경"
        ]
	},
	"U_47_PW_MAX_USE": {
		"path": ["cat /etc/login.defs"],
		"check_point": ["PASS_MAX_DAYS 90"],
        "cm_line": [
            "양호 조건: 패스워드 최대 사용기간이 90일(12주) 이하로 설정되어 있는 경우.",
            "예시:  PASS_MAX_DAYS 90",
            "보안 조치: vi /etc/login.defs PASS_MAX_DAYS 90로 변경"
        ]
	},
	"U_48_PW_MIN_USE": {
		"path": ["cat /etc/login.defs"],
		"check_point": ["PASS_MIN_DAYS 7"],
        "cm_line": [
            "양호 조건: 패스워드 최소 사용기간이 1일 이상 설정되어 있는 경우.",
            "예시: PASS_MIN_DAYS 7",
            "보안 조치: vi /etc/login.defs PASS_MIN_DAYS 7로 변경"
        ]
	},
	"U_49_NONE_USABLE_ID": {
		"path": ["cat /etc/passwd 2>/dev/null",
                 "cat /etc/passwd | egrep 'lp|uucp|nuucp' 2>/dev/null",
                 "cat /var/log/audit/audit.log 2>/dev/null",
                 "utmpdump /var/log/wtmp 2>/dev/null", ],
		"check_point": [""],
        "ex_line": [
            "양호 조건: 불필요한 계정이 존재하지 않는 경우.",
            "예시: 보고 판단",
            "보안 조치: 판단 후 userdel <user_name>"
        ]
	},
	"U_50_ROOT_MIN": {
		"path": ["cat /etc/group | grep root 2>/dev/null"],
		"check_point": [
            "양호 조건: 관리자 그룹에 불필요한 계정이 등록되어 있지 않은 경우",
            "예시: root:x:0:root",
            "보안 조치: vi /etc/group 으로 위 라인의 불필요한 계정 삭제"
        ],
		"just_line": [""]
	},
	"U_51_NON_GID": {
		"path": ["pass_2"],
		"check_point": "",
		"just_line": [""]
	},
	"U_52_DUP_UID": {
		"path": ["pass_2"],
		"check_point": "",
		"just_line": [""]
	},
	"U_53_USER_SHELL": {
		"path": ['egrep "^daemon|^bin|^sys|^adm|^listen|^nobody|^nobody4|^noaccess|^diag|^operator|^games|^gopher" /etc/passwd | grep -v "admin"'],
		"check_point": ["/sbin/nologin"],
        "cm_line": [
            "양호 조건: 로그인이 필요하지 않은 계정에 /bin/false(/sbin/nologin) 쉘이 부여되어 있는 경우.",
            "예시: daemon:x:1:1::/:/bin/false",
            "보안 조치: vi /etc/passwd 로 /bin/false 또는 :/sbin/nologin 로 변경"
        ]
	},
	"U_54_SESS_TIMEOUT": {
		"path": ["cat /etc/profile | grep TMOUT 2>/dev/null"],
		"check_point": ["TMOUT=600", "export TMOUT"],
		"cm_line": [
            "양호 조건: Session Timeout이 600초(10분) 이하로 설정되어 있는 경우",
            "예시: TMOUT=600, export TMOUT",
            "보안 조치: vi /etc/profile 으로 위 라인의 명시"
        ]
	},

	"U_55_CUPS": {
		"path": ["ls -l /etc/cups/cupsd.conf"],
		"check_point": ["-rw-r-----.","root"],
        "cm_line": [
            "양호 조건: hosts.lpd(cupsd.conf) 파일이 삭제되어 있거나 불가피하게 hosts.lpd(cupsd.conf) 파일을 사용할 시 파일의 소유자가 root이고 권한이 600인 경우.",
            "예시: daemon:x:1:1::/:/bin/false",
            "보안 조치: chown root, chmod 600"
        ]
	},

	"U_56_UMASK": {
		"path": ["cat /etc/profile"],
		"check_point": ["umask 022"],
		"cm_line": [
            "양호 조건: UMASK 값이 022 이상으로 설정된 경우.",
            "예시: umask 022",
            "보안 조치: vi /etc/profile로 변경"
        ]
	},

}
