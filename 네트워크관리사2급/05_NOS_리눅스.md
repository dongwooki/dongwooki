# 05. NOS ② Linux

> **과목:** NOS (Network Operating System)
> **출제 비중 체감:** ★★★★☆ (NOS 과목 중 절반 가까이가 리눅스. 명령어·권한·설정 파일은 거의 매 회 출제)
> **목표 공부시간:** 3~4시간 (본문 2.5시간 + 연습문제 1시간)

---

## 이 노트에서 다루는 것

- 리눅스의 특징과 구조 (커널 / 셸 / 파일시스템)
- 배포판 계열 (Red Hat 계열 vs Debian 계열)
- 셸의 종류
- 디렉터리 구조 (FHS)
- 파일·디렉터리 기본 명령어
- 파일 권한 (rwx, chmod, chown, umask, SetUID/SetGID/Sticky Bit)
- 사용자·그룹 관리 (/etc/passwd, /etc/shadow, /etc/group, useradd …)
- 프로세스 관리 (ps, top, kill, nice, 포그라운드/백그라운드)
- 부팅 과정과 서비스 관리 (GRUB2, systemd, 런레벨, systemctl)
- 패키지 관리 (rpm, yum/dnf, dpkg, apt)
- 파일시스템·디스크 (ext2/3/4, xfs, fdisk, mkfs, mount, /etc/fstab)
- 압축·아카이브 (tar, gzip, bzip2, xz)
- vi/vim 편집기
- 리다이렉션과 파이프
- 예약 작업 (cron, at)
- 로그 파일
- 네트워크 설정 명령과 설정 파일
- 주요 서버 데몬과 설정 파일 (Apache, Samba, NFS, BIND, SSH, vsftpd)
- 원격 접속 (ssh, scp)

---

## 1. 리눅스 개요와 특징

### 1-1. 리눅스란?

리눅스(Linux)는 **1991년 핀란드 헬싱키 대학의 리누스 토발즈(Linus Torvalds)** 가 만든 **유닉스(Unix) 계열 운영체제의 커널**이다.
엄밀히 말하면 "리눅스"는 커널(운영체제의 핵심)만을 가리키고, 여기에 GNU 프로젝트의 도구들(셸, 컴파일러, 유틸리티)을 합쳐 하나의 운영체제로 묶어 배포한 것이 우리가 쓰는 "리눅스 배포판"이다.

- **GNU 프로젝트**: 리처드 스톨먼(Richard Stallman)이 시작한 자유 소프트웨어 운동. FSF(자유 소프트웨어 재단)가 운영.
- **GPL(General Public License)**: 리눅스 커널의 라이선스. 소스 코드를 공개해야 하고, 누구나 자유롭게 사용·수정·재배포할 수 있다. 단, 수정해서 배포하면 그 결과물도 GPL로 소스를 공개해야 한다.

### 1-2. 리눅스의 특징 (시험에 그대로 나옴)

| 특징 | 설명 |
|---|---|
| **오픈 소스** | 소스 코드가 공개(GPL). 누구나 수정·재배포 가능 |
| **멀티유저(다중 사용자)** | 여러 사용자가 동시에 접속해서 사용 가능 |
| **멀티태스킹(다중 작업)** | 여러 프로그램(프로세스)을 동시에 실행 |
| **멀티프로세서 지원** | 여러 CPU(SMP) 지원 |
| **유닉스 호환 / POSIX 준수** | 유닉스 명령어·프로그램과 호환성이 높음 |
| **다양한 파일시스템 지원** | ext2/3/4, xfs, FAT, NTFS(읽기/쓰기 지원 도구), ISO9660 등 |
| **네트워크 기능 강력** | TCP/IP를 기본 내장. 서버 OS로 많이 사용 |
| **가상 메모리(스왑) 지원** | 물리 메모리가 부족하면 디스크의 swap 영역을 메모리처럼 사용 |
| **계층적 파일 구조** | 최상위 `/`(루트)에서 시작하는 트리 구조 |
| **모듈 방식 커널** | 모놀리식 커널이지만 필요한 기능(드라이버)을 모듈로 동적 적재 가능 (`lsmod`, `modprobe`, `insmod`, `rmmod`) |
| **이식성** | 대부분 C 언어로 작성되어 다양한 하드웨어로 이식 쉬움 |

> 💡 시험 포인트: "리눅스의 특징으로 옳지 **않은** 것" — "소스 비공개", "단일 사용자", "특정 하드웨어 전용" 같은 선지가 오답으로 나온다.

### 1-3. 리눅스의 구조 (3계층)

```
   ┌──────────────────────────────┐
   │  사용자 / 응용 프로그램        │
   ├──────────────────────────────┤
   │  셸 (Shell) ─ 명령어 해석기    │  ← 사용자 명령을 커널이 이해하도록 해석
   ├──────────────────────────────┤
   │  커널 (Kernel) ─ 핵심          │  ← 프로세스·메모리·파일시스템·장치 관리
   ├──────────────────────────────┤
   │  하드웨어                      │
   └──────────────────────────────┘
```

| 구성 요소 | 역할 |
|---|---|
| **커널(Kernel)** | 운영체제의 핵심. **프로세스 관리, 메모리 관리, 파일시스템 관리, 장치(디바이스 드라이버) 관리, 네트워크 관리** 담당. 부팅 시 메모리에 상주 |
| **셸(Shell)** | 사용자와 커널 사이의 **명령어 해석기(인터프리터)**. 사용자가 입력한 명령을 해석해 커널에 전달 |
| **파일시스템** | 파일과 디렉터리를 저장·관리하는 구조 |
| **유틸리티/응용 프로그램** | 편집기, 컴파일러, 각종 서버 프로그램 등 |

> 💡 시험 포인트: "사용자의 명령을 해석하여 커널에 전달하는 것은?" → **셸**. "메모리·프로세스·장치를 관리하는 핵심은?" → **커널**.

---

## 2. 배포판 계열

리눅스 커널 + GNU 도구 + 설치 프로그램 + 패키지 관리자를 묶어 배포하는 것이 **배포판(Distribution)** 이다. 시험에서는 **"어느 계열이 어떤 패키지 관리자를 쓰는가"** 를 묻는다.

| 계열 | 대표 배포판 | 패키지 형식 | 저수준 도구 | 고수준 도구(의존성 자동 해결) |
|---|---|---|---|---|
| **Red Hat 계열** | RHEL, CentOS, Fedora, Rocky Linux, AlmaLinux, Oracle Linux | `.rpm` | `rpm` | `yum` (구버전), `dnf` (RHEL 8 이후) |
| **Debian 계열** | Debian, Ubuntu, Linux Mint, Kali Linux | `.deb` | `dpkg` | `apt`, `apt-get` |
| SUSE 계열 | SUSE Linux Enterprise, openSUSE | `.rpm` | `rpm` | `zypper` |

- **CentOS**: RHEL을 무료로 재빌드한 배포판. CentOS Linux 지원 종료 후 그 자리를 **Rocky Linux / AlmaLinux** 가 대체.
- **Fedora**: Red Hat이 후원하는 커뮤니티 배포판. 신기술 테스트베드 성격.
- **Ubuntu**: Debian 기반. 데스크톱·서버 모두 많이 사용.

> 💡 시험 포인트: "Ubuntu – yum", "CentOS – apt" 처럼 계열을 엇갈려 놓은 선지가 오답.

---

## 3. 셸(Shell)의 종류

| 셸 | 경로 예 | 특징 |
|---|---|---|
| **sh (Bourne Shell)** | `/bin/sh` | 스티븐 본(Stephen Bourne)이 개발한 최초의 표준 유닉스 셸 |
| **bash (Bourne Again Shell)** | `/bin/bash` | sh를 확장한 GNU 셸. **대부분 리눅스 배포판의 기본 셸**. 명령 히스토리, 탭 자동완성, 별칭(alias) 지원 |
| **csh (C Shell)** | `/bin/csh` | 빌 조이(Bill Joy) 개발. **C 언어와 비슷한 문법** |
| **tcsh** | `/bin/tcsh` | csh의 개선판 (명령행 편집, 자동완성) |
| **ksh (Korn Shell)** | `/bin/ksh` | 데이비드 콘(David Korn) 개발. sh와 호환되며 csh 기능 일부 추가 |
| **zsh (Z Shell)** | `/bin/zsh` | bash·ksh·tcsh 기능을 합친 확장 셸 |

관련 명령·파일:

| 명령 / 파일 | 의미 |
|---|---|
| `echo $SHELL` | 현재 로그인 셸 확인 |
| `cat /etc/shells` | 시스템에서 **사용 가능한 셸 목록** |
| `chsh -s /bin/zsh` | 로그인 셸 변경 (change shell) |
| `~/.bashrc`, `~/.bash_profile` | 사용자별 bash 환경 설정 파일 |
| `/etc/profile`, `/etc/bashrc` | 전체 사용자 공통 환경 설정 파일 |

> 💡 시험 포인트: "리눅스 기본 셸, Bourne 셸 확장" → **bash**. "C 언어와 유사한 문법" → **csh**. "사용 가능한 셸 목록 파일" → **/etc/shells**.

---

## 4. 디렉터리 구조 (FHS: Filesystem Hierarchy Standard)

리눅스는 윈도우처럼 C:, D: 드라이브가 있는 게 아니라, **최상위 루트 디렉터리 `/` 하나에서 모든 것이 뻗어나가는 트리 구조**다. 다른 디스크도 특정 디렉터리에 "마운트(연결)"해서 쓴다.

| 디렉터리 | 용도 | 기억법 |
|---|---|---|
| `/` | 루트(최상위) 디렉터리 | 모든 것의 시작 |
| `/bin` | 일반 사용자도 쓰는 **기본 명령어** (ls, cp, mv, cat …) | **bin**ary |
| `/sbin` | **시스템 관리용 명령어** (root용: fdisk, ifconfig, reboot …) | **s**ystem bin |
| `/boot` | **커널 이미지(vmlinuz)**, 부트로더(GRUB) 설정 등 부팅 파일 | boot |
| `/dev` | **장치 파일** (/dev/sda, /dev/null, /dev/tty …) | **dev**ice |
| `/etc` | **시스템 설정 파일** (passwd, fstab, hosts …) | 설정은 etc |
| `/home` | **일반 사용자의 홈 디렉터리** (/home/user1) | home |
| `/root` | **root(관리자)의 홈 디렉터리** | `/`와 헷갈리지 말 것 |
| `/lib` | 공유 **라이브러리**, 커널 모듈(/lib/modules) | library |
| `/tmp` | **임시 파일**. 누구나 쓰기 가능 (Sticky Bit 설정) | temporary |
| `/usr` | 사용자 프로그램, 라이브러리, 문서 (/usr/bin, /usr/local …) | Unix System Resources |
| `/var` | **내용이 자주 바뀌는(가변) 파일**: 로그(/var/log), 메일 스풀, 프린터 스풀, 웹 문서(/var/www) | **var**iable |
| `/proc` | **가상 파일시스템**. 커널·프로세스 정보를 메모리에서 보여줌 (/proc/cpuinfo, /proc/meminfo). 디스크에 실제 저장 X | **proc**ess |
| `/mnt` | 임시 마운트 지점 | mount |
| `/media` | CD-ROM, USB 등 이동식 장치 자동 마운트 지점 | media |
| `/opt` | 추가 설치하는 **응용 프로그램(패키지)** | **opt**ional |
| `/lost+found` | fsck 검사 시 복구된 파일 조각 보관 | 분실물 보관소 |

> 💡 시험 포인트: 디렉터리–용도 연결 문제. 특히 **/etc(설정) · /var(로그) · /proc(가상, 프로세스 정보) · /dev(장치) · /boot(커널)** 는 반드시.

---

## 5. 파일·디렉터리 기본 명령어

### 5-1. 이동·확인

| 명령 | 기능 | 자주 나오는 옵션 |
|---|---|---|
| `pwd` | 현재 작업 디렉터리 출력 (print working directory) | |
| `cd` | 디렉터리 이동 | `cd ~` 홈, `cd ..` 상위, `cd -` 직전 위치, `cd /` 루트 |
| `ls` | 목록 보기 | `-a` 숨김 파일(.으로 시작) 포함, `-l` 자세히, `-R` 하위까지, `-h` 크기 사람이 읽기 쉽게, `-t` 수정 시간순, `-i` inode 번호, `-d` 디렉터리 자체 정보 |

### 5-2. 생성·복사·이동·삭제

| 명령 | 기능 | 옵션 |
|---|---|---|
| `mkdir` | 디렉터리 생성 | `-p` 상위 디렉터리까지 한 번에 생성 (`mkdir -p a/b/c`) |
| `rmdir` | **빈** 디렉터리 삭제 | 안에 파일이 있으면 실패 |
| `rm` | 파일 삭제 | `-r` 디렉터리까지 재귀 삭제, `-f` 묻지 않고 강제, `-i` 삭제 전 확인 |
| `cp` | 복사 | `-r`(또는 `-R`) 디렉터리 복사, `-p` 권한·시간 보존, `-i` 덮어쓰기 확인 |
| `mv` | 이동 **및 이름 변경** | `mv a.txt b.txt` = 이름 변경 |
| `touch` | **빈 파일 생성** 또는 기존 파일의 **시간 정보 갱신** | |

### 5-3. 내용 보기

| 명령 | 기능 |
|---|---|
| `cat` | 파일 내용 전체 출력 (여러 파일 연결: con**cat**enate) |
| `more` | 한 화면씩 출력 (앞으로만 이동) |
| `less` | 한 화면씩 출력 (앞뒤 자유 이동, more의 개선판) |
| `head` | 앞부분 출력 (기본 10줄, `-n 5` 5줄) |
| `tail` | 뒷부분 출력 (기본 10줄). **`tail -f`** : 파일 끝에 추가되는 내용을 실시간 출력 → 로그 모니터링에 사용 |
| `wc` | 줄·단어·바이트 수 세기 (`-l` 줄, `-w` 단어, `-c` 바이트) |

### 5-4. 검색

| 명령 | 기능 | 예시 |
|---|---|---|
| `find` | **파일을 조건으로 검색** | `find / -name "*.conf"`, `find / -type f -size +100M`, `find / -perm -4000` (SetUID 파일), `find /home -user kim`, `find . -mtime -7` (7일 이내 수정) |
| `grep` | **파일 내용에서 문자열(패턴) 검색** | `grep root /etc/passwd`, `-i` 대소문자 무시, `-v` 일치하지 **않는** 줄, `-n` 줄번호, `-r` 하위 디렉터리, `-c` 일치 줄 수 |
| `which` | PATH에서 **명령어 실행 파일 경로** 찾기 | `which ls` → /usr/bin/ls |
| `whereis` | 명령어의 **실행 파일 + 소스 + 매뉴얼(man) 위치** 모두 찾기 | `whereis ls` |
| `locate` | 미리 만든 DB에서 빠르게 파일 이름 검색 (`updatedb`로 갱신) | |

> 📌 **find vs grep** : find는 "파일 **이름·속성**"으로 찾고, grep은 "파일 **내용**"에서 찾는다.

### 5-5. 링크 (ln)

| 구분 | 하드 링크 (`ln 원본 링크`) | 심볼릭 링크 (`ln -s 원본 링크`) |
|---|---|---|
| inode | 원본과 **같은 inode** 공유 | **별도 inode** (원본 경로만 저장) |
| 원본 삭제 시 | 데이터 그대로 접근 가능 (링크 수만 감소) | **링크가 깨짐** (접근 불가) |
| 다른 파일시스템(파티션) | **불가** | 가능 |
| 디렉터리 링크 | 불가 | 가능 |
| ls -l 표시 | 일반 파일(`-`)과 동일, 링크 수 증가 | 맨 앞 `l`, `링크 -> 원본` 표시 |
| 비유 | 같은 집에 문을 하나 더 냄 | 윈도우 "바로 가기" |

> 💡 시험 포인트: 명령어 기능 매칭(특히 `pwd`, `touch`, `mv`=이름변경, `rmdir`=빈 디렉터리만, `tail -f`, `find` vs `grep`)과 하드/심볼릭 링크 차이.

---

## 6. 파일 권한 (가장 많이 나오는 파트!)

### 6-1. ls -l 출력 읽기

```
-rwxr-xr--  1  kim  dev  2048  Oct 27 10:00  run.sh
│└┬┘└┬┘└┬┘  │   │    │    │        │           └ 파일 이름
│ │  │  │   │   │    │    │        └ 수정 시간
│ │  │  │   │   │    │    └ 크기(바이트)
│ │  │  │   │   │    └ 소유 그룹
│ │  │  │   │   └ 소유자
│ │  │  │   └ 하드 링크 수
│ │  │  └ 기타 사용자(other) 권한: r--
│ │  └ 그룹(group) 권한: r-x
│ └ 소유자(user) 권한: rwx
└ 파일 종류
```

**파일 종류(첫 글자)**

| 기호 | 종류 |
|---|---|
| `-` | 일반 파일 |
| `d` | 디렉터리 |
| `l` | 심볼릭 링크 |
| `b` | 블록 장치 파일 (디스크 등, /dev/sda) |
| `c` | 문자 장치 파일 (터미널 등, /dev/tty) |
| `s` | 소켓 |
| `p` | 파이프 (FIFO) |

### 6-2. 권한의 의미와 숫자 표기

| 권한 | 숫자 | 파일에서 | 디렉터리에서 |
|---|---|---|---|
| `r` (read) | **4** | 내용 읽기 | 목록 보기(ls) |
| `w` (write) | **2** | 내용 수정 | 안에 파일 생성·삭제 |
| `x` (execute) | **1** | 실행 | 디렉터리 진입(cd) |

**계산법:** 각 자리(소유자/그룹/기타)에서 있는 권한의 숫자를 더한다.

| 문자 | 계산 | 숫자 |
|---|---|---|
| `rwx` | 4+2+1 | 7 |
| `rw-` | 4+2+0 | 6 |
| `r-x` | 4+0+1 | 5 |
| `r--` | 4+0+0 | 4 |
| `-wx` | 0+2+1 | 3 |
| `---` | 0 | 0 |

예) `rwxr-xr--` → 7 / 5 / 4 → **754**
예) `rw-r--r--` → 6 / 4 / 4 → **644**
예) `chmod 640` → `rw-r-----`

### 6-3. chmod (권한 변경)

**① 숫자 모드**
```bash
chmod 755 script.sh      # rwxr-xr-x
chmod 600 secret.txt     # rw-------
chmod -R 755 /data       # 하위 전체 재귀 적용
```

**② 기호 모드**: `[대상][연산자][권한]`

| 대상 | 의미 | 연산자 | 의미 |
|---|---|---|---|
| `u` | user(소유자) | `+` | 권한 추가 |
| `g` | group | `-` | 권한 제거 |
| `o` | other(기타) | `=` | 지정한 권한으로 **설정**(나머지 제거) |
| `a` | all(모두) | | |

```bash
chmod u+x run.sh          # 소유자에게 실행 권한 추가
chmod g-w file            # 그룹의 쓰기 권한 제거
chmod o=r file            # 기타 사용자는 읽기만
chmod a+r file            # 모두에게 읽기 추가
chmod u=rwx,g=rx,o= file  # = 750
```

### 6-4. chown / chgrp (소유자·그룹 변경)

```bash
chown kim file.txt          # 소유자를 kim으로
chown kim:dev file.txt      # 소유자 kim, 그룹 dev로 동시에
chown -R kim:dev /data      # 하위 전체
chgrp dev file.txt          # 그룹만 dev로
```
- 소유자 변경(chown)은 원칙적으로 **root만** 가능.

### 6-5. umask (기본 권한 결정)

새 파일·디렉터리가 만들어질 때 **기본 최대 권한에서 umask 값을 빼서** 실제 권한이 정해진다.

| 대상 | 기본 최대 권한 | umask 022일 때 | umask 027일 때 | umask 077일 때 |
|---|---|---|---|---|
| **디렉터리** | 777 | **755** | **750** | 700 |
| **파일** | 666 (실행권한 기본 없음) | **644** | **640** | 600 |

- `umask` : 현재 값 확인 / `umask 027` : 값 변경
- root의 기본 umask는 보통 **022**.
- 정확히는 "빼기"가 아니라 umask 비트를 **제거(마스킹)** 하는 것이지만, 시험 수준에서는 빼기로 계산하면 된다. (예외: 파일에 umask 033처럼 홀수 자리가 있으면 666-033=633이 아니라 644. 시험에선 거의 안 나옴)

### 6-6. 특수 권한 (SetUID / SetGID / Sticky Bit)

| 특수 권한 | 숫자 | 표시 위치 | 의미 | 대표 예 |
|---|---|---|---|---|
| **SetUID** | **4000** | 소유자 x 자리 → `s` | 실행하는 동안 **파일 소유자(주로 root)의 권한**으로 실행 | `/usr/bin/passwd` (`-rwsr-xr-x`) — 일반 사용자가 /etc/shadow를 수정할 수 있는 이유 |
| **SetGID** | **2000** | 그룹 x 자리 → `s` | 실행하는 동안 **파일 소유 그룹의 권한**으로 실행. 디렉터리에 걸면 안에 생성되는 파일이 디렉터리 그룹을 상속 | 공유 디렉터리 |
| **Sticky Bit** | **1000** | 기타 x 자리 → `t` | 디렉터리에 설정. **누구나 파일을 만들 수 있지만, 삭제·이름변경은 그 파일의 소유자(와 root)만** 가능 | `/tmp` (`drwxrwxrwt`, 1777) |

```bash
chmod 4755 prog     # -rwsr-xr-x  (SetUID)
chmod 2755 prog     # -rwxr-sr-x  (SetGID)
chmod 1777 /share   # drwxrwxrwt  (Sticky)
chmod u+s prog      # 기호로 SetUID
chmod g+s dir       # 기호로 SetGID
chmod o+t dir       # 기호로 Sticky
```
- 대문자 `S`, `T` : 특수 권한은 있는데 **그 자리의 실행 권한(x)이 없는** 상태.
- `find / -perm -4000` : SetUID가 설정된 파일 찾기 (보안 점검용).

> 💡 시험 포인트: ① 문자↔숫자 권한 변환, ② umask 계산, ③ `s`/`t`가 무엇인지, ④ `-rwsr-xr-x` = **4755**, `/tmp` = **1777**.

---

## 7. 사용자·그룹 관리

### 7-1. 핵심 파일 3총사

**① /etc/passwd** — 사용자 계정 정보 (누구나 읽기 가능, 644)

```
kim:x:1001:1001:Kim Dev:/home/kim:/bin/bash
 ①  ② ③    ④     ⑤        ⑥         ⑦
```

| 번호 | 필드 | 설명 |
|---|---|---|
| ① | 사용자 이름 | 로그인 ID |
| ② | 패스워드 | `x` = 실제 암호는 /etc/shadow에 있음 |
| ③ | **UID** | 사용자 번호. **root = 0**, 시스템 계정은 낮은 번호, 일반 사용자는 보통 1000부터(RHEL 7 이후) |
| ④ | **GID** | 기본(주) 그룹 번호 |
| ⑤ | 설명(GECOS) | 이름, 연락처 등 코멘트 |
| ⑥ | 홈 디렉터리 | |
| ⑦ | 로그인 셸 | `/sbin/nologin` 또는 `/bin/false`면 로그인 불가 계정 |

**② /etc/shadow** — **암호화된 패스워드**와 패스워드 정책 (root만 읽기 가능)

```
kim:$6$abc...:19650:0:99999:7:::
 ① ②         ③    ④  ⑤    ⑥ ⑦⑧⑨
```
① 사용자명 ② 암호화된 패스워드(`!`·`*`면 잠김/사용 불가) ③ 마지막 변경일(1970.1.1 기준 일수) ④ 최소 사용 기간 ⑤ 최대 사용 기간 ⑥ 만료 경고 일수 ⑦ 만료 후 비활성 유예 일수 ⑧ 계정 만료일 ⑨ 예약

**③ /etc/group** — 그룹 정보
```
dev:x:1100:kim,lee
 ①  ② ③   ④
```
① 그룹명 ② 그룹 패스워드(x → /etc/gshadow) ③ GID ④ 그룹에 속한 사용자 목록(보조 그룹 멤버)

**기타 관련 파일**

| 파일 | 역할 |
|---|---|
| `/etc/skel` | 새 사용자 생성 시 **홈 디렉터리로 복사되는 기본 환경 파일(.bashrc 등)의 원본** 보관 디렉터리 |
| `/etc/login.defs` | UID/GID 범위, 패스워드 만료 기본 정책, 메일 디렉터리 등 **계정 생성 기본값** |
| `/etc/default/useradd` | useradd 기본값 (기본 홈 위치, 기본 셸 등) |
| `/etc/sudoers` | sudo 권한 설정 (`visudo`로 편집) |

### 7-2. 사용자·그룹 명령어

| 명령 | 기능 | 주요 옵션 |
|---|---|---|
| `useradd` | 사용자 생성 | `-d` 홈 디렉터리 지정, `-s` 셸 지정, `-g` 기본 그룹, `-G` 보조 그룹, `-u` UID 지정, `-m` 홈 디렉터리 생성, `-e` 만료일 |
| `usermod` | 사용자 정보 수정 | `-aG dev kim` (dev 그룹에 추가), `-s`, `-d`, `-l`(이름 변경), `-L`(잠금) |
| `userdel` | 사용자 삭제 | **`-r` 홈 디렉터리와 메일 스풀까지 삭제** |
| `passwd` | 패스워드 설정/변경 | `passwd kim`(root가 kim 비번 설정), `-l` 잠금, `-u` 잠금 해제, `-d` 비번 삭제 |
| `chage` | 패스워드 만료 정책 변경 | `-l` 정보 확인, `-M` 최대 일수 |
| `groupadd` / `groupdel` / `groupmod` | 그룹 생성/삭제/수정 | `-g` GID 지정 |
| `id` | 사용자의 **UID, GID, 소속 그룹** 출력 | `id kim` |
| `whoami` | 현재 사용자 이름 | |
| `who`, `w` | 현재 로그인한 사용자 목록 | |

### 7-3. su vs sudo

| 구분 | su | sudo |
|---|---|---|
| 의미 | **다른 사용자로 전환**(switch user). 기본은 root | **명령 하나만 root 권한으로 실행** |
| 필요 비밀번호 | **전환할 대상(root)의 비밀번호** | **자기 자신의 비밀번호** |
| 설정 | - | `/etc/sudoers` (wheel 그룹 등) |
| 비고 | `su -` : 대상 사용자의 **로그인 환경(환경변수, 홈)까지** 불러옴. `su`만 쓰면 현재 환경 유지 | 실행 기록이 로그에 남아 관리에 유리 |

> 💡 시험 포인트: /etc/passwd 필드 순서(특히 3번째 UID, 4번째 GID, 7번째 셸), 암호 저장 위치(/etc/shadow), /etc/skel 용도, `userdel -r`.

---

## 8. 프로세스 관리

**프로세스** = 실행 중인 프로그램. 각 프로세스는 고유 번호 **PID**를 가진다.
- **PID 1** = 부팅 시 커널이 가장 먼저 실행하는 프로세스 → 최신 배포판은 **systemd**, 옛날에는 **init**. 모든 프로세스의 조상.
- **데몬(daemon)** = 백그라운드에서 계속 실행되며 요청을 기다리는 서비스 프로세스. 이름이 보통 `d`로 끝남 (httpd, sshd, named, crond …).
- **부모/자식 프로세스**: 프로세스는 fork로 자식을 만든다. PPID = 부모 PID.

### 8-1. 확인 명령

| 명령 | 기능 |
|---|---|
| `ps` | 현재 프로세스 스냅샷. `ps aux`(BSD 스타일, 모든 사용자 프로세스 상세), `ps -ef`(System V 스타일, PPID 포함 전체 목록) |
| `top` | **실시간** 프로세스·CPU·메모리 사용량 모니터링 (`q` 종료) |
| `pstree` | 프로세스 부모-자식 관계를 트리로 |
| `pgrep` | 이름으로 PID 찾기 |

### 8-2. 시그널과 kill

`kill [-시그널] PID` : 프로세스에 시그널을 보낸다. (꼭 "죽이는" 것만이 아니라 신호 전달)

| 번호 | 이름 | 의미 |
|---|---|---|
| **1** | SIGHUP | 터미널 끊김 / 데몬에게는 **설정 파일 다시 읽기(재시작)** 용도 |
| **2** | SIGINT | 인터럽트 = 키보드 **Ctrl + C** |
| **9** | SIGKILL | **무조건 강제 종료** (무시·차단 불가) |
| **15** | SIGTERM | **정상 종료 요청 — kill의 기본값** (시그널 생략 시) |
| 20 | SIGTSTP | 일시 정지 = 키보드 **Ctrl + Z** |

```bash
kill 1234        # = kill -15 1234 (정상 종료 요청)
kill -9 1234     # 강제 종료
killall httpd    # 이름으로 같은 이름의 프로세스 모두 종료
pkill -u kim     # 조건(사용자 등)으로 종료
kill -l          # 시그널 목록
```

### 8-3. 포그라운드 / 백그라운드 작업

| 명령/키 | 기능 |
|---|---|
| `명령 &` | 명령을 **백그라운드**로 실행 |
| `Ctrl + Z` | 포그라운드 작업 일시 정지 |
| `jobs` | 현재 셸의 작업 목록 (작업번호 %1, %2…) |
| `fg %1` | 1번 작업을 **포그라운드**로 |
| `bg %1` | 정지된 1번 작업을 **백그라운드**에서 계속 실행 |
| `nohup 명령 &` | **로그아웃해도 종료되지 않게** 실행 (출력은 nohup.out) |

### 8-4. 우선순위 (nice / renice)

- **nice 값 범위: -20 ~ 19**, 기본값 **0**
- **값이 작을수록(음수일수록) 우선순위가 높다** (CPU를 더 받음). "nice(착하다)할수록 양보한다" → 값이 클수록 양보 = 우선순위 낮음.
- 일반 사용자는 nice 값을 **올리기(우선순위 낮추기)만** 가능. 음수로 내리는 것은 **root만**.

```bash
nice -n 10 ./job.sh        # nice 값 10으로 실행
renice -5 -p 1234          # 실행 중인 PID 1234의 nice 값을 -5로 변경 (root)
```

> 💡 시험 포인트: kill 기본 시그널(15), 강제 종료(9), nice 범위(-20~19)와 방향, `&`·`fg`·`bg`·`nohup` 기능.

---

## 9. 부팅 과정과 서비스 관리

### 9-1. 부팅 순서

```
전원 ON → BIOS/UEFI (POST: 하드웨어 자가진단)
       → 부트로더 GRUB2 (MBR/GPT에서 로드, 커널 선택)
       → 커널 로드 (initramfs로 드라이버 준비, 루트 파일시스템 마운트)
       → systemd (PID 1) 실행 (옛날: init)
       → default.target(런레벨)에 따라 서비스 시작 → 로그인 화면
```

- **부트로더**: 커널을 메모리에 올려주는 프로그램. 현재 표준은 **GRUB2**, 과거에는 **LILO**, GRUB(Legacy).
- GRUB2 설정: `/etc/default/grub` 수정 → `grub2-mkconfig -o /boot/grub2/grub.cfg` 로 반영 (grub.cfg 직접 수정 X).

### 9-2. 런레벨과 systemd target

| 런레벨 | 의미 | systemd target |
|---|---|---|
| **0** | 시스템 종료(halt) | `poweroff.target` |
| **1** | 단일 사용자 모드 (복구용, root만) | `rescue.target` |
| 2 | 다중 사용자 (NFS 없음) | `multi-user.target` |
| **3** | **다중 사용자, 텍스트(CLI) 모드** — 서버 기본 | **`multi-user.target`** |
| 4 | 사용 안 함 (사용자 정의) | `multi-user.target` |
| **5** | **그래픽(GUI) 모드** — X Window | **`graphical.target`** |
| **6** | **재부팅** | `reboot.target` |

```bash
systemctl get-default                      # 기본 target 확인
systemctl set-default multi-user.target    # 부팅 시 텍스트 모드로
systemctl isolate graphical.target         # 지금 바로 GUI로 전환
init 3 / init 6                            # 옛 방식 런레벨 전환
runlevel                                   # 현재 런레벨 확인
```
- 과거(SysV init) 기본 런레벨 설정 파일: `/etc/inittab`

### 9-3. systemctl (서비스 관리)

| 명령 | 기능 |
|---|---|
| `systemctl start httpd` | 서비스 **지금 시작** |
| `systemctl stop httpd` | 서비스 중지 |
| `systemctl restart httpd` | 재시작 |
| `systemctl reload httpd` | 서비스를 끊지 않고 설정만 다시 읽기 |
| `systemctl status httpd` | 상태 확인 (active/inactive, 최근 로그) |
| `systemctl enable httpd` | **부팅 시 자동 시작 등록** |
| `systemctl disable httpd` | 부팅 시 자동 시작 해제 |
| `systemctl is-enabled httpd` | 자동 시작 여부 확인 |
| `systemctl list-units --type=service` | 서비스 목록 |

> 📌 **start ≠ enable** : start는 "지금 켜기", enable은 "다음 부팅부터 자동으로 켜기". 둘 다 하려면 `systemctl enable --now httpd`.
> 옛 방식: `service httpd start`, `chkconfig httpd on`.

### 9-4. 종료·재부팅

| 명령 | 기능 |
|---|---|
| `shutdown -h now` | 지금 종료 (halt) |
| `shutdown -r now` | 지금 재부팅 |
| `shutdown -h +10` | 10분 후 종료 |
| `shutdown -h 22:00` | 22시에 종료 |
| `shutdown -c` | 예약된 종료 취소 |
| `reboot` / `init 6` | 재부팅 |
| `halt` / `poweroff` / `init 0` | 종료 |

> 💡 시험 포인트: 런레벨 번호 ↔ 의미 ↔ target, `systemctl enable` vs `start`, `shutdown` 옵션, 부트로더(GRUB/LILO).

---

## 10. 패키지 관리

### 10-1. RPM (Red Hat 계열 저수준 도구)

파일 이름 형식: `httpd-2.4.57-5.el9.x86_64.rpm` → **이름-버전-릴리스.아키텍처.rpm**

| 명령 | 기능 |
|---|---|
| `rpm -ivh 파일.rpm` | **설치** (i=install, v=상세, h=진행 표시 #) |
| `rpm -Uvh 파일.rpm` | **업그레이드** (없으면 설치) |
| `rpm -Fvh 파일.rpm` | 이미 설치된 경우에만 업그레이드 |
| `rpm -e 패키지명` | **삭제** (erase) |
| `rpm -qa` | **설치된 모든 패키지 목록** (query all) |
| `rpm -qi 패키지명` | 패키지 상세 정보 |
| `rpm -ql 패키지명` | 패키지가 설치한 파일 목록 |
| `rpm -qf /경로/파일` | 이 파일이 어느 패키지 소속인지 |
| `rpm -V 패키지명` | 설치 파일 무결성 검증 |

- rpm은 **의존성을 자동 해결하지 못한다** → 그래서 yum/dnf가 등장.

### 10-2. yum / dnf (Red Hat 계열 고수준 도구)

- 인터넷 **저장소(repository)** 에서 패키지를 내려받고 **의존성까지 자동 해결**.
- 저장소 설정: `/etc/yum.repos.d/*.repo`
- `dnf`는 yum의 후속 (RHEL 8+, Fedora). 명령 문법 거의 동일.

```bash
yum install httpd     # 설치
yum remove httpd      # 삭제
yum update            # 전체 업데이트
yum list installed    # 설치 목록
yum search nginx      # 검색
yum info httpd        # 정보
```

### 10-3. dpkg / apt (Debian 계열)

| 명령 | 기능 |
|---|---|
| `dpkg -i 파일.deb` | 설치 |
| `dpkg -r 패키지` | 삭제 (설정 파일 남김), `-P` 설정까지 완전 삭제(purge) |
| `dpkg -l` | 설치 목록 |
| `apt update` | **저장소 패키지 목록(인덱스) 갱신** (실제 업그레이드 아님!) |
| `apt upgrade` | 설치된 패키지 실제 업그레이드 |
| `apt install 패키지` | 설치 (의존성 자동 해결) |
| `apt remove 패키지` | 삭제 |

> 💡 시험 포인트: `rpm -ivh`(설치) / `-Uvh`(업그레이드) / `-e`(삭제) / `-qa`(목록), 배포판–패키지 도구 매칭.

---

## 11. 파일시스템과 디스크

### 11-1. 리눅스 파일시스템 종류

| 파일시스템 | 특징 |
|---|---|
| **ext2** | 리눅스 전통 파일시스템. **저널링 기능 없음** → 비정상 종료 시 fsck 검사 오래 걸림 |
| **ext3** | ext2 + **저널링(Journaling)** 추가. ext2와 호환 |
| **ext4** | ext3 개선. 대용량 파일·볼륨 지원, extent 방식, 빠른 fsck. 많은 배포판의 기본 |
| **xfs** | 고성능 64비트 저널링 파일시스템. **RHEL/CentOS 7 이후 기본** |
| **swap** | 가상 메모리용 영역 (파일시스템이라기보다 스왑 공간) |
| vfat / ntfs | 윈도우 호환 |
| iso9660 | CD-ROM |
| nfs | 네트워크 파일시스템 |

> 📌 **저널링(Journaling)** : 데이터를 실제 디스크에 쓰기 전에 "무엇을 쓸지"를 **저널(로그)에 먼저 기록**. 갑자기 전원이 꺼져도 저널을 보고 빠르게 복구 → 파일시스템 무결성 향상, 부팅 시 검사 시간 단축.

### 11-2. 장치 이름 규칙

| 장치명 | 의미 |
|---|---|
| `/dev/sda` | 첫 번째 SATA/SCSI/USB 디스크 |
| `/dev/sdb` | 두 번째 디스크 |
| `/dev/sda1` | 첫 번째 디스크의 **첫 번째 파티션** |
| `/dev/hda` | (옛날) 첫 번째 IDE 디스크 |
| `/dev/nvme0n1p1` | 첫 NVMe SSD의 첫 파티션 |
| `/dev/cdrom`, `/dev/sr0` | CD/DVD |

- MBR 방식: 주(Primary) 파티션 최대 **4개** (확장 파티션 사용 시 그 안에 논리 파티션). 논리 파티션 번호는 5번부터(sda5). GPT 방식은 기본 128개.

### 11-3. 디스크 작업 순서와 명령

```
① 파티션 생성      fdisk /dev/sdb        (GPT 대용량: gdisk, parted)
② 파일시스템 생성   mkfs -t ext4 /dev/sdb1  또는 mkfs.ext4 /dev/sdb1, mkfs.xfs
③ 마운트          mount /dev/sdb1 /data
④ 영구 등록       /etc/fstab 에 한 줄 추가
```

| 명령 | 기능 |
|---|---|
| `fdisk -l` | 디스크·파티션 목록 확인 |
| `mkfs` | 파일시스템 생성(포맷) |
| `mkswap /dev/sdb2` / `swapon` / `swapoff` | 스왑 영역 생성/활성/비활성 |
| `mount` | 장치를 디렉터리에 연결 (`mount -t iso9660 /dev/cdrom /mnt/cdrom`), 인자 없이 실행하면 현재 마운트 목록 |
| `umount` | 마운트 해제 (**unmount 아님, n 없음!**) |
| `df -h` | **파일시스템(파티션)별 디스크 사용량/남은 공간** |
| `du -sh /home` | **특정 디렉터리(파일)가 차지하는 용량** |
| `fsck` / `e2fsck` | 파일시스템 검사·복구 (마운트 해제 상태에서) |
| `blkid` | 장치의 UUID·파일시스템 종류 확인 |
| `free -h` | 메모리·스왑 사용량 |

> 📌 **df vs du** : **df** = **d**isk **f**ree (파티션 단위 전체 사용량), **du** = **d**isk **u**sage (디렉터리 단위 사용량).

### 11-4. /etc/fstab (부팅 시 자동 마운트 설정)

```
/dev/sdb1    /data    ext4    defaults    1    2
   ①           ②       ③        ④        ⑤    ⑥
```

| 번호 | 필드 | 설명 |
|---|---|---|
| ① | 장치명 | /dev/sdb1 또는 `UUID=...`, `LABEL=...` |
| ② | 마운트 포인트 | 연결할 디렉터리 |
| ③ | 파일시스템 종류 | ext4, xfs, swap, nfs … |
| ④ | 마운트 옵션 | `defaults`(rw, suid, dev, exec, auto, nouser, async), `ro`, `noexec`, `usrquota` … |
| ⑤ | **dump** | dump 명령으로 **백업할지** (1=백업, 0=안 함) |
| ⑥ | **fsck 순서** | 부팅 시 **파일시스템 검사 순서** (루트=1, 그 외=2, 0=검사 안 함) |

- 현재 마운트 상태는 `/etc/mtab` 또는 `/proc/mounts` 에서 확인.

> 💡 시험 포인트: ext2(저널링 X) vs ext3(저널링 O), fstab 6필드 순서, `df`/`du` 구분, `/dev/sda1` 의미.

---

## 12. 압축과 아카이브

- **아카이브(묶기)**: 여러 파일을 하나로 묶기만 함 (크기 안 줄어듦) → **tar**
- **압축**: 크기를 줄임 → **gzip, bzip2, xz** (보통 파일 하나만 압축)
- 그래서 리눅스는 "tar로 묶고 → gzip으로 압축" = `.tar.gz` (`.tgz`)

### 12-1. tar 옵션

| 옵션 | 의미 |
|---|---|
| `c` | **c**reate: 묶기(생성) |
| `x` | e**x**tract: 풀기 |
| `t` | lis**t**: 내용 목록 보기 |
| `v` | **v**erbose: 처리 과정 출력 |
| `f` | **f**ile: 아카이브 파일 이름 지정 (**반드시 마지막 옵션 뒤에 파일명**) |
| `z` | **gzip** 압축/해제 (.tar.gz) |
| `j` | **bzip2** 압축/해제 (.tar.bz2) |
| `J` | **xz** 압축/해제 (.tar.xz) |
| `C` | 풀 위치 지정 (`-C /tmp`) |

```bash
tar cvf backup.tar /home          # 묶기
tar xvf backup.tar                # 풀기
tar tvf backup.tar                # 목록 보기
tar zcvf backup.tar.gz /home      # 묶고 gzip 압축
tar zxvf backup.tar.gz            # gzip 해제하고 풀기
tar jcvf backup.tar.bz2 /home     # bzip2
tar Jxvf backup.tar.xz            # xz
```

### 12-2. 압축 명령

| 압축 | 해제 | 확장자 | 비고 |
|---|---|---|---|
| `gzip file` | `gunzip file.gz` / `gzip -d` | `.gz` | 가장 흔함. 원본 파일이 압축 파일로 **대체됨** |
| `bzip2 file` | `bunzip2 file.bz2` / `bzip2 -d` | `.bz2` | gzip보다 압축률 높고 느림 |
| `xz file` | `unxz file.xz` / `xz -d` | `.xz` | 압축률 가장 높음 |
| `zip a.zip files` | `unzip a.zip` | `.zip` | 윈도우 호환 |

> 💡 시험 포인트: `c`=묶기, `x`=풀기, `z`=gzip, `j`=bzip2, `f`=파일 지정. "tar.gz 파일을 푸는 명령은?" → `tar zxvf`.

---

## 13. vi / vim 편집기

### 13-1. 세 가지 모드

```
            i, a, o 등
 [명령 모드] ─────────→ [입력 모드]
  (일반모드)  ←───────── (텍스트 입력)
     │           ESC
     │ :  (콜론)
     ↓
 [라스트 라인 모드(ex 모드)]  → 저장/종료/검색·치환/설정
```

| 모드 | 하는 일 | 진입 |
|---|---|---|
| **명령 모드** | 커서 이동, 삭제, 복사, 붙여넣기 (vi 시작 시 기본 모드) | 입력 모드에서 `ESC` |
| **입력 모드** | 글자 입력 | `i`, `a`, `o` 등 |
| **라스트 라인(ex) 모드** | 저장, 종료, 치환, 환경 설정 | 명령 모드에서 `:` |

### 13-2. 자주 나오는 키

**입력 모드로 전환**

| 키 | 동작 |
|---|---|
| `i` | 커서 **앞**에 입력 (insert) |
| `a` | 커서 **뒤**에 입력 (append) |
| `o` | 커서 **아래 새 줄** 만들어 입력 |
| `O` | 커서 **위 새 줄** |
| `I` / `A` | 줄 맨 앞 / 줄 맨 끝에서 입력 |

**명령 모드 편집**

| 키 | 동작 |
|---|---|
| `x` | 커서 위치 한 글자 삭제 |
| `dd` | **한 줄 삭제(잘라내기)**, `3dd` 세 줄 |
| `yy` | **한 줄 복사**(yank), `3yy` 세 줄 |
| `p` / `P` | 커서 아래(뒤) / 위(앞)에 **붙여넣기** |
| `u` | 실행 취소(undo) |
| `gg` / `G` | 파일 처음 / 끝으로 |
| `h j k l` | ← ↓ ↑ → 이동 |
| `/문자열` | **아래 방향 검색**, `n` 다음 결과, `N` 이전 |
| `?문자열` | 위 방향 검색 |

**라스트 라인 모드**

| 명령 | 동작 |
|---|---|
| `:w` | 저장 |
| `:q` | 종료 (변경 사항 있으면 거부) |
| `:q!` | **저장하지 않고 강제 종료** |
| `:wq` / `:x` / (명령모드) `ZZ` | **저장 후 종료** |
| `:w 새이름` | 다른 이름으로 저장 |
| `:set nu` (`:set number`) | 줄 번호 표시, `:set nonu` 해제 |
| `:%s/old/new/g` | 파일 전체에서 old를 new로 **치환** |
| `:10` | 10번째 줄로 이동 |

> 💡 시험 포인트: 모드 3가지 이름, `i/a/o` 차이, `dd`/`yy`/`p`, `:q!` vs `:wq`, `/` 검색, `:set nu`.

---

## 14. 리다이렉션과 파이프

모든 프로세스는 3개의 기본 입출력 통로를 가진다.

| 번호 | 이름 | 기본 연결 |
|---|---|---|
| 0 | 표준 입력 (stdin) | 키보드 |
| 1 | 표준 출력 (stdout) | 화면 |
| 2 | 표준 에러 (stderr) | 화면 |

| 기호 | 의미 | 예시 |
|---|---|---|
| `>` | 출력을 파일로 (**덮어쓰기**, 없으면 생성) | `ls > list.txt` |
| `>>` | 출력을 파일 끝에 **추가(append)** | `date >> log.txt` |
| `<` | 파일을 입력으로 | `sort < names.txt` |
| `2>` | **에러 메시지만** 파일로 | `find / -name a 2> err.txt` |
| `2>&1` | 에러를 표준 출력과 같은 곳으로 | `cmd > all.txt 2>&1` |
| `&>` | 표준 출력 + 에러 모두 | `cmd &> all.txt` |
| `\|` | **파이프**: 앞 명령의 출력을 뒤 명령의 입력으로 | `ps aux \| grep httpd`, `cat /etc/passwd \| wc -l` |
| `/dev/null` | 출력 버리는 "블랙홀" 장치 | `cmd > /dev/null 2>&1` |

> 💡 시험 포인트: `>`(덮어쓰기) vs `>>`(추가), `2>`(에러), `|`(파이프).

---

## 15. 예약 작업 (cron / at)

### 15-1. cron — **반복** 예약

- 데몬: `crond`
- `crontab -e` 편집 / `crontab -l` 목록 / `crontab -r` 삭제 / `crontab -u kim -e` 다른 사용자(root)
- 시스템 전체: `/etc/crontab` (사용자 필드가 하나 더 있음), `/etc/cron.d/`, `/etc/cron.daily/` 등
- 사용 허가/거부: `/etc/cron.allow`, `/etc/cron.deny`

**5개 시간 필드 + 명령**
```
 분   시   일   월   요일   명령
 *    *    *    *    *     /path/command
0-59 0-23 1-31 1-12  0-7 (0과 7 = 일요일, 1=월요일 … 6=토요일)
```

| 기호 | 의미 |
|---|---|
| `*` | 매(모든 값) |
| `,` | 여러 값 (1,15) |
| `-` | 범위 (1-5) |
| `/` | 간격 (*/10 = 10마다) |

| 예시 | 의미 |
|---|---|
| `0 3 * * * cmd` | 매일 03:00 |
| `30 2 * * 0 cmd` | 매주 **일요일** 02:30 |
| `*/10 * * * * cmd` | 10분마다 |
| `0 9 * * 1-5 cmd` | 평일(월~금) 09:00 |
| `0 0 1 * * cmd` | 매월 1일 00:00 |
| `0 12 1 1 * cmd` | 매년 1월 1일 12:00 |

### 15-2. at — **한 번만** 예약

- 데몬: `atd`
- `at 22:00` / `at now + 10 minutes` 입력 후 명령, `Ctrl+D`로 종료
- `atq` 예약 목록, `atrm 번호` 삭제

> 💡 시험 포인트: crontab 필드 순서(**분 시 일 월 요일**)와 해석. cron=반복, at=1회.

---

## 16. 로그 파일

로그는 대부분 **/var/log** 아래에 있다. (rsyslog 데몬이 기록, 설정 `/etc/rsyslog.conf`)

| 파일 | 내용 |
|---|---|
| `/var/log/messages` | **시스템 전반의 일반 메시지** (Red Hat 계열) |
| `/var/log/secure` | **인증·보안 관련**(로그인 성공/실패, su, sshd) (Red Hat 계열) |
| `/var/log/syslog`, `/var/log/auth.log` | Debian/Ubuntu에서 위 두 파일에 해당 |
| `/var/log/boot.log` | 부팅 시 서비스 시작 메시지 |
| `/var/log/dmesg` | 부팅 시 커널 메시지 |
| `/var/log/maillog` | 메일 로그 |
| `/var/log/cron` | cron 실행 기록 |
| `/var/log/wtmp` | 로그인/로그아웃 이력 (바이너리 → **`last`** 명령으로 확인) |
| `/var/log/btmp` | **로그인 실패** 기록 (→ **`lastb`**) |
| `/var/log/lastlog` | 사용자별 마지막 로그인 (→ **`lastlog`**) |
| `/var/log/httpd/` | Apache access_log, error_log |

| 명령 | 기능 |
|---|---|
| `dmesg` | **커널 링 버퍼 메시지**(하드웨어 인식, 드라이버) 출력 |
| `journalctl` | **systemd 저널** 로그 조회 (`-u httpd` 특정 서비스, `-f` 실시간, `-b` 이번 부팅) |
| `tail -f /var/log/messages` | 로그 실시간 확인 |

> 💡 시험 포인트: messages(일반) vs secure(인증), `last`/`lastb`, `dmesg`.

---

## 17. 네트워크 설정 (명령과 파일)

### 17-1. 설정 명령

| 명령 | 기능 |
|---|---|
| `ifconfig` | (구식, net-tools) 인터페이스 IP 확인·설정. `ifconfig eth0 192.168.1.10 netmask 255.255.255.0 up` |
| `ip addr show` (`ip a`) | (신식, iproute2) **IP 주소 확인** |
| `ip addr add 192.168.1.10/24 dev eth0` | IP 추가 |
| `ip link set eth0 up/down` | 인터페이스 활성/비활성 |
| `ifup eth0` / `ifdown eth0` | 인터페이스 켜기/끄기 |
| `hostname` | 호스트 이름 확인 (임시 변경) |
| `hostnamectl set-hostname srv1` | 호스트 이름 **영구** 변경 (/etc/hostname 수정) |
| `nmcli` | **NetworkManager 명령줄 도구** (`nmcli con show`, `nmcli con mod ...`, `nmcli dev status`) |
| `nmtui` | NetworkManager 텍스트 메뉴 UI |

### 17-2. 네트워크 설정 파일

| 파일 | 내용 |
|---|---|
| `/etc/hosts` | **IP ↔ 호스트 이름**을 직접 매핑 (DNS보다 먼저 참조하는 로컬 이름표) |
| `/etc/resolv.conf` | **사용할 DNS 서버(네임서버) 주소** 지정 (`nameserver 8.8.8.8`, `search example.com`) |
| `/etc/hostname` | 호스트 이름 |
| `/etc/nsswitch.conf` (`/etc/host.conf`) | 이름 해석 순서 (hosts: files dns → /etc/hosts 먼저, 다음 DNS) |
| `/etc/services` | **서비스 이름 ↔ 포트 번호** 대응표 (ssh 22/tcp …) |
| `/etc/protocols` | 프로토콜 이름 ↔ 번호 |
| `/etc/sysconfig/network-scripts/ifcfg-eth0` | Red Hat 계열(RHEL 8 이하) **인터페이스별 IP 설정 파일** (BOOTPROTO=static/dhcp, IPADDR, NETMASK/PREFIX, GATEWAY, ONBOOT=yes) |
| `/etc/sysconfig/network` | Red Hat 계열 전체 네트워크 설정 (호스트명, 게이트웨이) |
| `/etc/NetworkManager/system-connections/` | RHEL 9 이후 NetworkManager 연결 프로필 |
| `/etc/network/interfaces`, `/etc/netplan/*.yaml` | Debian / Ubuntu 인터페이스 설정 |

> 💡 시험 포인트: **/etc/hosts(로컬 이름 매핑) vs /etc/resolv.conf(DNS 서버 주소)** 구분, `ifcfg-eth0` 위치, `/etc/services`.
> (ping, traceroute, netstat, nslookup 등 진단 명령은 TCP/IP 노트에서 다룬다.)

---

## 18. 주요 서버 데몬과 설정 파일

| 서비스 | 패키지/데몬 | 주요 설정 파일 | 핵심 내용 |
|---|---|---|---|
| **웹(Apache)** | `httpd` (Debian: apache2) | **`/etc/httpd/conf/httpd.conf`** | `Listen 80`, `DocumentRoot "/var/www/html"`(웹 문서 위치), `ServerName`, `DirectoryIndex index.html` |
| **파일 공유(윈도우와)** | **Samba** — `smbd`, `nmbd` | **`/etc/samba/smb.conf`** | **SMB/CIFS** 프로토콜로 리눅스↔윈도우 파일·프린터 공유. 사용자 등록 `smbpasswd -a kim` |
| **파일 공유(유닉스 간)** | **NFS** — `nfs-server` | **`/etc/exports`** | 공유 디렉터리와 허용 호스트 지정 `/data 192.168.1.0/24(rw,sync)`. `exportfs -a` 적용, `showmount -e 서버` 확인, 클라이언트는 `mount -t nfs 서버:/data /mnt` |
| **DNS** | **BIND** — `named` | **`/etc/named.conf`**, 존 파일 `/var/named/` | 도메인 이름 ↔ IP 변환 서버 |
| **원격 접속** | OpenSSH — `sshd` | **`/etc/ssh/sshd_config`** | `Port 22`, `PermitRootLogin no`(root 직접 로그인 금지), `PasswordAuthentication` |
| **FTP** | **vsftpd** | `/etc/vsftpd/vsftpd.conf` | `anonymous_enable=NO`(익명 접속 금지), `local_enable`, `write_enable`. 접속 거부 사용자 목록 `/etc/vsftpd/ftpusers` |
| **DHCP** | `dhcpd` | `/etc/dhcp/dhcpd.conf` | IP 자동 할당 범위(range) 설정 |
| **메일** | sendmail / postfix | `/etc/mail/sendmail.cf`, `/etc/postfix/main.cf` | |
| **시간 동기화** | chronyd | `/etc/chrony.conf` | |

> 📌 **Samba vs NFS** : Samba는 **윈도우와** 공유(SMB/CIFS), NFS는 **유닉스/리눅스끼리** 공유.

> 💡 시험 포인트: 서비스 ↔ 설정 파일 매칭. 특히 **httpd.conf, smb.conf, /etc/exports, named.conf, sshd_config**.

---

## 19. 원격 접속 (ssh / scp)

| 명령 | 기능 |
|---|---|
| `ssh kim@192.168.1.10` | kim 계정으로 원격 서버에 **암호화** 접속 |
| `ssh -p 2222 kim@host` | 다른 포트로 접속 |
| `scp file.txt kim@host:/tmp/` | 로컬 → 원격으로 **파일 복사** (SSH 기반 암호화) |
| `scp kim@host:/etc/hosts .` | 원격 → 로컬로 복사 |
| `scp -r dir kim@host:/tmp/` | 디렉터리 복사 |
| `ssh-keygen` | 공개키/개인키 쌍 생성 (키 기반 로그인) |
| `ssh-copy-id kim@host` | 공개키를 원격 서버의 `~/.ssh/authorized_keys`에 등록 |
| `sftp kim@host` | SSH 기반 대화형 파일 전송 |

- telnet, rlogin, rsh 등은 **평문 전송**이라 보안상 ssh로 대체.

> 💡 시험 포인트: "원격 서버에 암호화된 채널로 파일을 복사하는 명령" → **scp**.

---

## ★ 핵심사항 (시험 직전 10분 암기용)

- 리눅스 = 리누스 토발즈(1991), **GPL 오픈소스**, 멀티유저·멀티태스킹, 유닉스 계열.
- 구조: **커널**(프로세스·메모리·장치 관리) ↔ **셸**(명령어 해석기) ↔ 사용자.
- 기본 셸 = **bash**, C 문법 = **csh**, 셸 목록 = **/etc/shells**, 셸 변경 = **chsh**.
- Red Hat 계열 = **rpm / yum / dnf**, Debian 계열 = **dpkg / apt**.
- **/etc** 설정, **/var** 로그·가변, **/proc** 가상(프로세스·커널 정보), **/dev** 장치, **/boot** 커널, **/root** root 홈, **/tmp** 임시(1777).
- `pwd` 현재 위치, `touch` 빈 파일/시간 갱신, `mv` 이동+이름변경, `rmdir` 빈 디렉터리만, `mkdir -p` 상위까지.
- `find` = 이름·속성 검색, `grep` = 내용 검색(`-v` 반전, `-i` 대소문자 무시).
- 하드 링크 = **같은 inode**, 파일시스템 넘기 불가 / 심볼릭(`ln -s`) = 별도 inode, 원본 삭제 시 깨짐.
- 권한 r=4, w=2, x=1 → `rwxr-xr--` = **754**, `rw-r--r--` = **644**.
- umask 022 → 디렉터리 **755** / 파일 **644**, umask 027 → **750** / **640**.
- SetUID **4000**(`s` 소유자 자리, 예: passwd), SetGID **2000**(`s` 그룹 자리), Sticky **1000**(`t`, 예: /tmp).
- /etc/passwd 7필드: **이름:x:UID:GID:설명:홈:셸**, root UID = **0**.
- 암호화된 비밀번호 = **/etc/shadow**, 그룹 = /etc/group, 신규 사용자 기본 파일 = **/etc/skel**, 계정 기본 정책 = **/etc/login.defs**.
- `userdel -r` = 홈 디렉터리까지 삭제, `usermod -aG` = 보조 그룹 추가, `id` = UID/GID/그룹 확인.
- `su -` = 대상 사용자 환경까지 전환(대상 비번), `sudo` = 명령 단위 root 실행(내 비번, /etc/sudoers).
- kill 기본 = **15(SIGTERM)**, 강제 = **9(SIGKILL)**, 설정 재읽기 = **1(SIGHUP)**, Ctrl+C = 2.
- nice **-20(최고) ~ 19(최저)**, 기본 0, 음수 설정은 root만. 실행 중 변경 = `renice`.
- `&` 백그라운드, `jobs`, `fg`, `bg`, `nohup`(로그아웃 후에도 실행), PID 1 = **systemd**.
- 부팅: BIOS/UEFI → **GRUB2** → 커널 → **systemd** → target.
- 런레벨 0 종료 / 1 단일 사용자 / 3 텍스트 다중 사용자(**multi-user.target**) / 5 GUI(**graphical.target**) / 6 재부팅.
- `systemctl start`(지금 시작) vs `enable`(부팅 시 자동 시작).
- `rpm -ivh` 설치, `-Uvh` 업그레이드, `-e` 삭제, `-qa` 전체 목록, `-qf` 파일 소속 패키지.
- ext2 = 저널링 **X**, ext3 = 저널링 **O**, ext4 = 개선판, xfs = RHEL 7+ 기본.
- fstab 6필드: **장치 / 마운트포인트 / 종류 / 옵션 / dump / fsck순서**.
- `df` = 파티션별 사용량, `du` = 디렉터리 사용량, `umount`(n 없음).
- tar: `c` 묶기, `x` 풀기, `t` 목록, `z` gzip, `j` bzip2, `J` xz, `f` 파일명 → `tar zxvf a.tar.gz`.
- vi 3모드: 명령 / 입력 / 라스트라인. `i`앞 `a`뒤 `o`아래줄, `dd` 줄삭제, `yy` 줄복사, `p` 붙여넣기, `:q!` 강제종료, `:wq` 저장종료, `/` 검색, `:set nu`.
- `>` 덮어쓰기, `>>` 추가, `2>` 에러, `|` 파이프.
- crontab: **분 시 일 월 요일**, 요일 0(7)=일요일. cron 반복 / at 1회.
- /var/log/**messages** 일반, /var/log/**secure** 인증, `last`(wtmp), `lastb`(btmp 실패), `dmesg` 커널, `journalctl` systemd.
- **/etc/hosts** 로컬 이름매핑, **/etc/resolv.conf** DNS 서버 주소, **/etc/services** 서비스–포트.
- 설정 파일: Apache **httpd.conf**, Samba **smb.conf**, NFS **/etc/exports**, BIND **named.conf**, SSH **sshd_config**, FTP **vsftpd.conf**.
- Samba = 윈도우와 공유(SMB/CIFS), NFS = 유닉스끼리 공유.

---

## ⚠️ 헷갈리는 함정 포인트

| 헷갈리는 쌍 | 구분법 |
|---|---|
| `/root` vs `/` | `/`는 최상위 루트 디렉터리, `/root`는 root **사용자의 홈** |
| `/bin` vs `/sbin` | bin = 일반 사용자 명령, sbin = **시스템 관리자** 명령 |
| `/etc/passwd` vs `/etc/shadow` | passwd엔 `x`만, **실제 암호화 비번은 shadow** (root만 읽기) |
| `/etc/hosts` vs `/etc/resolv.conf` | hosts = **이름↔IP 직접 매핑**, resolv.conf = **DNS 서버 주소** |
| `find` vs `grep` | find = 파일 **이름/속성**, grep = 파일 **내용** |
| `which` vs `whereis` | which = 실행 파일 경로만, whereis = 실행·소스·**man 페이지**까지 |
| `rm -r` vs `rmdir` | rmdir은 **빈** 디렉터리만 삭제 |
| `>` vs `>>` | `>` 덮어쓰기, `>>` 끝에 추가 |
| `systemctl start` vs `enable` | start = 지금, enable = 부팅 시 자동 |
| `kill` 기본 vs `kill -9` | 기본은 15번 정상 종료 요청, 9번은 강제 |
| nice 값 크기 | **작을수록 우선순위 높음**. 범위 -20~19 (0~99 아님!) |
| umask 계산 | 디렉터리는 777에서, **파일은 666에서** 뺀다 |
| SetUID vs SetGID 표시 | 둘 다 `s`! **소유자 자리면 SetUID**, 그룹 자리면 SetGID. Sticky만 `t` |
| `s` vs `S` | 소문자 = 특수권한 + 실행권한 있음, 대문자 = 실행권한 없음 |
| 하드 링크 vs 심볼릭 링크 | 같은 inode = 하드, 원본 지우면 깨지는 것 = 심볼릭 |
| ext2 vs ext3 | **저널링 유무** (ext2 없음) |
| fstab 5번째 vs 6번째 필드 | 5 = **dump(백업)**, 6 = **fsck 순서** |
| `df` vs `du` | df = 파티션(free), du = 디렉터리(usage) |
| `tar c` vs `tar x` | c = create(묶기), x = extract(풀기) |
| vi `:q` vs `:q!` vs `:wq` | `:q`는 변경 있으면 거부, `:q!` 버리고 종료, `:wq` 저장 후 종료 |
| vi `i` vs `a` vs `o` | 커서 앞 / 커서 뒤 / 아랫줄 |
| crontab 3번째 vs 5번째 필드 | 3 = **일(날짜)**, 5 = **요일** (0=일요일) |
| cron vs at | cron = 반복, at = 한 번 |
| Samba vs NFS | Samba = 윈도우 공유(smb.conf), NFS = 리눅스끼리(/etc/exports) |
| `su` vs `su -` | `-` 붙으면 대상 사용자의 **로그인 환경까지** |
| apt update vs apt upgrade | update = **목록 갱신만**, upgrade = 실제 업그레이드 |
| 런레벨 1 vs 3 vs 5 | 1 = 단일 사용자(복구), 3 = 텍스트 다중 사용자, 5 = GUI |
| messages vs secure | messages = 일반 시스템, secure = **로그인·인증** |

---

## 🧠 암기 팁

- **권한 숫자 "4-2-1 읽쓰실"** : **r**ead 4, **w**rite 2, e**x**ecute 1 → "읽(4)고 쓰(2)고 실행(1)".
- **특수권한 "4UID-2GID-1스티키"** : "**사(4)용자 이(2)그룹 일(1)스티키**" → SetUID 4, SetGID 2, Sticky 1. 위치도 순서대로 소유자 / 그룹 / 기타.
- **/etc/passwd 7필드** : "**이 x U G 설 홈 셸**" (이름, x, UID, GID, 설명, 홈, 셸) — "이엑스 유지 설홈셸".
- **fstab 6필드** : "**장 마 종 옵 덤 검**" (장치, 마운트, 종류, 옵션, 덤프, 검사) — "장마철 종옵(좀) 덤검".
- **crontab 5필드** : "**분 시 일 월 요**" — "분시일월요" = 작은 단위 → 큰 단위 → 요일.
- **nice** : "착할(nice)수록 양보한다" → 값이 클수록 우선순위 **낮음**.
- **kill 9** : "구(9)사일생 없음, 무조건 죽음" / **15**는 "일오(15)… 정중하게 종료 요청".
- **런레벨** : "**0 끄기, 1 혼자, 3 텍스트, 5 그림, 6 다시**".
- **tar 옵션** : "**c**reate · e**x**tract · lis**t** / **z**=gzip, **j**=bzip2(**j**는 b 다음…), **f**는 file 이름은 맨 뒤".
- **df/du** : "**f**ree(파티션 남은 공간) / **u**sage(디렉터리 사용량)".
- **vi 입력** : "**i**n(안쪽=앞), **a**fter(뒤), **o**pen line(새 줄)".
- **로그** : "**s**ecure = **s**ecurity(로그인 기록)".
- **Samba** : "삼바 춤은 **윈**도우 앞에서" → 윈도우 공유.

---

## 📝 연습문제 (과거 기출 유형 변형, 25문항)

**[리눅스-01]** 리눅스(Linux)에 대한 설명으로 옳지 **않은** 것은?
① 리누스 토발즈가 개발한 커널을 기반으로 한 유닉스 계열 운영체제이다.
② GPL 라이선스에 따라 소스 코드가 공개되어 자유롭게 수정·재배포할 수 있다.
③ 여러 사용자가 동시에 접속하여 여러 작업을 수행하는 멀티유저·멀티태스킹을 지원한다.
④ 커널 소스가 비공개이므로 하드웨어 제조사만 디바이스 드라이버를 개발할 수 있다.

**[리눅스-02]** Bourne Shell(sh)을 확장하여 만든 GNU 셸로, 명령 히스토리와 탭 자동완성 기능을 제공하며 대부분의 리눅스 배포판에서 기본 셸로 사용되는 것은?
① bash
② csh
③ ksh
④ tcsh

**[리눅스-03]** 주로 시스템 관리자(root)가 사용하는 **시스템 관리용 명령어**(fdisk, reboot, ifconfig 등)가 저장된 디렉터리는?
① /bin
② /sbin
③ /dev
④ /opt

**[리눅스-04]** `chmod 754 report.sh` 명령을 실행한 후 report.sh 파일의 권한을 문자로 표시한 것으로 옳은 것은?
① rwxr-xr--
② rwxr-xr-x
③ rwxrw-r--
④ rw-r-xr--

**[리눅스-05]** umask 값이 027로 설정된 상태에서 새로 생성한 **디렉터리**의 기본 권한은?
① 640
② 755
③ 750
④ 777

**[리눅스-06]** `ls -l` 결과가 `-rwsr-xr-x` 로 표시되는 파일의 권한을 숫자(8진수)로 나타낸 것은?
① 2755
② 4755
③ 1755
④ 6755

**[리눅스-07]** 다음은 `/tmp` 디렉터리를 `ls -ld` 로 확인한 결과이다. 마지막 자리의 `t` 에 대한 설명으로 옳은 것은?
```
drwxrwxrwt  10 root root 4096 Oct 27 09:00 /tmp
```
① SetUID로, 파일 실행 시 소유자(root)의 권한으로 실행된다.
② SetGID로, 디렉터리 안에 생성되는 파일이 root 그룹을 상속한다.
③ 기타 사용자에게 실행 권한이 없음을 나타낸다.
④ Sticky Bit로, 누구나 파일을 생성할 수 있지만 삭제는 파일 소유자와 root만 할 수 있다.

**[리눅스-08]** /etc/passwd 파일의 한 줄이 다음과 같을 때, 세 번째 필드인 `1001` 이 의미하는 것은?
```
kim:x:1001:1100:Kim Dev:/home/kim:/bin/bash
```
① 기본 그룹 ID(GID)
② 사용자 ID(UID)
③ 패스워드 최대 사용 기간
④ 암호화된 패스워드

**[리눅스-09]** 리눅스에서 사용자의 **암호화된 패스워드**와 패스워드 만료 정보가 저장되며, root만 읽을 수 있는 파일은?
① /etc/passwd
② /etc/group
③ /etc/shadow
④ /etc/login.defs

**[리눅스-10]** `useradd` 명령으로 새 사용자를 만들 때 사용자의 홈 디렉터리로 복사되는 `.bashrc`, `.bash_profile` 등 기본 환경 파일의 원본이 들어 있는 디렉터리는?
① /etc/skel
② /etc/default
③ /home/skel
④ /usr/local/etc

**[리눅스-11]** 사용자 계정 `lee` 를 삭제하면서 해당 사용자의 홈 디렉터리와 메일 스풀까지 함께 삭제하려고 한다. `userdel` 명령에 사용할 옵션은?
① -d
② -h
③ -m
④ -r

**[리눅스-12]** 정상 종료 요청에 응답하지 않는 프로세스(PID 2048)를 **무조건 강제 종료**하기 위한 명령으로 옳은 것은?
① kill -1 2048
② kill -2 2048
③ kill -9 2048
④ kill -15 2048

**[리눅스-13]** 리눅스 프로세스의 nice 값에 대한 설명으로 옳은 것은?
① nice 값의 범위는 -20 ~ 19이며 값이 작을수록 우선순위가 높다.
② nice 값의 범위는 0 ~ 99이며 값이 클수록 우선순위가 높다.
③ 일반 사용자도 자신의 프로세스 nice 값을 음수로 낮출 수 있다.
④ 이미 실행 중인 프로세스의 nice 값은 변경할 수 없다.

**[리눅스-14]** systemd를 사용하는 리눅스에서 기존 SysV init의 **런레벨 3**(텍스트 모드 다중 사용자)에 해당하는 target은?
① graphical.target
② rescue.target
③ reboot.target
④ multi-user.target

**[리눅스-15]** 웹 서버 서비스(httpd)가 **시스템 부팅 시 자동으로 시작**되도록 설정하는 명령은?
① systemctl start httpd
② systemctl enable httpd
③ systemctl status httpd
④ systemctl reload httpd

**[리눅스-16]** Red Hat 계열 리눅스에서 **현재 시스템에 설치된 모든 RPM 패키지 목록**을 확인하는 명령은?
① rpm -ivh
② rpm -e
③ rpm -Uvh
④ rpm -qa

**[리눅스-17]** 리눅스 배포판과 기본 패키지 관리 도구의 연결이 옳지 **않은** 것은?
① Ubuntu – yum
② Rocky Linux – dnf
③ Debian – apt
④ CentOS 7 – yum

**[리눅스-18]** 다음 /etc/fstab 항목에서 다섯 번째 필드 `1` 이 의미하는 것은?
```
/dev/sdb1    /data    ext4    defaults    1    2
```
① 마운트 옵션
② 파일시스템 종류
③ dump 명령에 의한 백업 대상 여부
④ 부팅 시 fsck 파일시스템 검사 순서

**[리눅스-19]** 리눅스 시스템이 도메인 이름을 질의할 **DNS 서버(네임서버)의 IP 주소**를 `nameserver` 항목으로 지정하는 파일은?
① /etc/hosts
② /etc/resolv.conf
③ /etc/services
④ /etc/hostname

**[리눅스-20]** gzip으로 압축된 아카이브 파일 `backup.tar.gz` 의 압축을 풀고 묶음을 해제하는 명령으로 옳은 것은?
① tar -cvf backup.tar.gz
② tar -tvf backup.tar.gz
③ tar -zcvf backup.tar.gz
④ tar -zxvf backup.tar.gz

**[리눅스-21]** vi 편집기에서 수정한 내용을 **저장하지 않고 강제로 종료**하는 명령은?
① :wq
② :w
③ :q!
④ ZZ

**[리눅스-22]** crontab에 다음과 같이 등록했을 때 /root/check.sh 가 실행되는 주기는?
```
*/10 * * * * /root/check.sh
```
① 10분마다
② 매시 10분
③ 매일 10시
④ 매월 10일

**[리눅스-23]** 명령 실행 중 발생하는 **오류 메시지만** error.log 파일로 저장하려고 한다. 빈칸에 들어갈 기호는?
```
find / -name a.txt ( ) error.log
```
① >
② 2>
③ <
④ |

**[리눅스-24]** 리눅스의 하드 링크와 심볼릭 링크에 대한 설명으로 옳은 것은?
① 하드 링크는 다른 파일시스템(파티션)에 있는 파일에도 만들 수 있다.
② 심볼릭 링크는 원본 파일을 삭제해도 링크를 통해 원본 데이터에 접근할 수 있다.
③ 하드 링크는 원본 파일과 같은 inode 번호를 공유한다.
④ 심볼릭 링크는 `ln -h` 옵션으로 생성한다.

**[리눅스-25]** 리눅스 서버 서비스와 주요 설정 파일의 연결이 옳지 **않은** 것은?
① Apache 웹 서버 – httpd.conf
② Samba – smb.conf
③ NFS – /etc/exports
④ BIND(DNS) – sshd_config

---

## ✅ 정답 및 해설

| 문항 | 정답 | 해설 |
|---|---|---|
| 리눅스-01 | ④ | 리눅스는 GPL 오픈소스로 커널 소스가 **공개**되어 누구나 드라이버·기능을 개발할 수 있다. ①②③은 리눅스의 대표 특징. |
| 리눅스-02 | ① | **bash**(Bourne Again Shell)는 sh를 확장한 GNU 셸로 대부분 배포판 기본 셸. csh는 C 언어 유사 문법, ksh는 Korn 셸, tcsh는 csh 개선판. |
| 리눅스-03 | ② | **/sbin** = system binaries(관리자용 명령). /bin은 일반 사용자도 쓰는 기본 명령(ls, cp 등), /dev는 장치 파일, /opt는 추가 응용 프로그램 설치 위치. |
| 리눅스-04 | ① | 7=rwx(4+2+1), 5=r-x(4+1), 4=r-- → **rwxr-xr--**. ②는 755, ③은 764, ④는 654. |
| 리눅스-05 | ③ | 디렉터리 기본 최대 권한 777 − 027 = **750**. 640은 같은 umask에서 **파일**의 권한(666−027 → 640). |
| 리눅스-06 | ② | 소유자 실행 자리의 `s` = **SetUID(4000)**, 나머지 rwxr-xr-x = 755 → **4755**. 2755는 SetGID, 1755는 Sticky, 6755는 SetUID+SetGID. |
| 리눅스-07 | ④ | 기타 사용자 실행 자리의 `t` = **Sticky Bit(1000)**. /tmp는 1777로 누구나 쓰기 가능하지만 남의 파일은 삭제 불가. SetUID/SetGID는 `s`로 표시. |
| 리눅스-08 | ② | /etc/passwd 필드 순서: 이름:x:**UID**:GID:설명:홈:셸 → 3번째는 UID. GID는 4번째(1100). 암호는 shadow에 있고, 만료 기간도 shadow 항목. |
| 리눅스-09 | ③ | 암호화된 패스워드는 **/etc/shadow**에 저장(root만 읽기). /etc/passwd에는 `x`만 표시. /etc/group은 그룹, /etc/login.defs는 계정 생성 기본 정책. |
| 리눅스-10 | ① | **/etc/skel**의 파일들이 새 사용자 홈 디렉터리로 복사된다. /etc/default/useradd는 useradd 기본값 파일일 뿐 환경 파일 원본이 아님. |
| 리눅스-11 | ④ | `userdel -r` = 홈 디렉터리와 메일 스풀까지 삭제. -d, -h, -m은 userdel에서 해당 기능의 옵션이 아니다(-d·-m은 useradd/usermod에서 홈 디렉터리 관련 옵션). |
| 리눅스-12 | ③ | **9번 SIGKILL**은 프로세스가 무시할 수 없는 강제 종료. 1(SIGHUP)=재시작/설정 재읽기, 2(SIGINT)=Ctrl+C, 15(SIGTERM)=kill 기본값인 정상 종료 요청. |
| 리눅스-13 | ① | nice 범위 **-20~19**, 값이 작을수록 우선순위 높음. 0~99는 아님, 음수 설정은 **root만** 가능, 실행 중인 프로세스는 **renice**로 변경 가능. |
| 리눅스-14 | ④ | 런레벨 2·3·4 → **multi-user.target**. graphical=5, rescue=1, reboot=6. |
| 리눅스-15 | ② | **enable** = 부팅 시 자동 시작 등록. start는 지금 시작(재부팅 후 유지 X), status는 상태 확인, reload는 설정 다시 읽기. |
| 리눅스-16 | ④ | `rpm -qa` = query all, 설치된 전체 목록. -ivh 설치, -e 삭제, -Uvh 업그레이드. |
| 리눅스-17 | ① | Ubuntu는 Debian 계열이므로 **apt/dpkg** 사용. yum은 Red Hat 계열(CentOS 7 등) 도구. Rocky Linux는 dnf, Debian은 apt가 맞다. |
| 리눅스-18 | ③ | fstab 필드: 장치 / 마운트포인트 / 종류 / 옵션 / **dump** / fsck 순서 → 5번째는 **dump 백업 여부**. 6번째 `2`가 fsck 검사 순서. |
| 리눅스-19 | ② | **/etc/resolv.conf**에 `nameserver IP`로 DNS 서버 지정. /etc/hosts는 IP↔호스트명 직접 매핑, /etc/services는 서비스–포트 대응표, /etc/hostname은 호스트 이름. |
| 리눅스-20 | ④ | `z`(gzip) + `x`(extract) + `v` + `f` → **tar -zxvf**. -cvf는 묶기, -tvf는 목록 보기, -zcvf는 gzip으로 묶어 압축 생성. |
| 리눅스-21 | ③ | **:q!** = 변경 사항 버리고 강제 종료. :wq와 ZZ는 저장 후 종료, :w는 저장만. |
| 리눅스-22 | ① | 첫 번째 필드(분)의 **`*/10` = 10분 간격**(0, 10, 20 … 50분). 매시 10분은 `10 * * * *`, 매일 10시는 `0 10 * * *`, 매월 10일은 `0 0 10 * *`. |
| 리눅스-23 | ② | 파일 디스크립터 **2 = 표준 에러(stderr)** → `2>`로 오류만 파일에 저장. `>`(=1>)는 표준 출력, `<`는 입력, `|`는 파이프. (출력+오류 모두 저장은 `> 파일 2>&1`) |
| 리눅스-24 | ③ | 하드 링크는 원본과 **같은 inode**를 공유한다. 하드 링크는 다른 파일시스템에 만들 수 없고(①×), 심볼릭 링크는 원본 삭제 시 깨지며(②×), 생성 옵션은 `ln -s`(④×). |
| 리눅스-25 | ④ | BIND(DNS)의 설정 파일은 **/etc/named.conf**. sshd_config는 SSH 서버(sshd) 설정 파일. |

**정답 분포:** ① 6개 · ② 6개 · ③ 6개 · ④ 7개
