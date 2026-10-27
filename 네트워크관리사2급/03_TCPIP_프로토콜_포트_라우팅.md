# 03. TCP/IP ② 프로토콜 · 포트 · 라우팅

> **과목:** TCP/IP
> **출제 비중 체감:** ★★★★★ (TCP/IP 과목 문제의 절반 이상이 이 노트에서 나옴)
> **목표 공부시간:** 3~4시간 (포트 번호 표는 시험 당일 아침에 한 번 더)

---

## 이 노트에서 다루는 것

- 1. TCP/IP 4계층과 계층별 프로토콜 분류
- 2. ARP / RARP (주소 변환)
- 3. ICMP / IGMP (제어·오류 메시지, 멀티캐스트)
- 4. TCP (헤더, 3-way handshake, 4-way 종료, 흐름·혼잡 제어)
- 5. UDP 와 TCP vs UDP 비교
- 6. 포트 번호 (시험 단골 표)
- 7. 응용 계층 프로토콜 상세 (HTTP, FTP, 메일, DNS, DHCP, SNMP, Telnet/SSH, TFTP, NTP)
- 8. 라우팅 (정적/동적, 거리벡터/링크상태, RIP·OSPF·EIGRP·IS-IS·BGP, 관리거리, 루프 방지)
- 9. 네트워크 진단 명령어 (ping, tracert, pathping, netstat, nslookup, ipconfig, arp, route)

> IP 주소 클래스·서브넷팅·IPv4/IPv6 헤더는 **02번 노트**에서 다룹니다.

---

## 1. TCP/IP 4계층과 프로토콜 분류

### 1-1. 왜 계층을 나누나?

네트워크 통신은 "전기 신호 보내기 → 목적지 찾아가기 → 빠짐없이 전달하기 → 프로그램끼리 대화하기"라는 여러 일을 한꺼번에 해야 합니다. 이걸 층(계층)으로 나눠서 각 층이 자기 일만 하도록 만든 것이 계층 모델입니다. OSI는 7계층(이론용), TCP/IP는 4계층(실제 인터넷용)입니다.

### 1-2. OSI 7계층 ↔ TCP/IP 4계층 대응

| OSI 7계층 | TCP/IP 4계층 | 데이터 단위(PDU) | 주요 프로토콜 |
|---|---|---|---|
| 7 응용 / 6 표현 / 5 세션 | **응용 계층 (Application)** | 메시지(데이터) | HTTP, FTP, SMTP, POP3, IMAP, DNS, DHCP, SNMP, Telnet, SSH, TFTP, NTP |
| 4 전송 | **전송 계층 (Transport)** | 세그먼트(TCP) / 데이터그램(UDP) | **TCP, UDP** |
| 3 네트워크 | **인터넷 계층 (Internet)** | 패킷(데이터그램) | **IP, ICMP, IGMP, ARP, RARP** |
| 2 데이터링크 / 1 물리 | **네트워크 접근 계층 (Network Access / Link)** | 프레임 / 비트 | Ethernet, PPP, Token Ring 등 |

> ARP/RARP는 엄밀히 말하면 2계층과 3계층 사이에서 동작하지만, **시험에서는 "인터넷 계층" 프로토콜로 분류**합니다. 헷갈리면 "IP 주소를 다루니까 인터넷 계층"으로 외우세요.

### 1-3. IP 패킷 안의 "프로토콜 번호" (참고)

IP 헤더의 Protocol 필드는 "이 패킷 안에 뭐가 들어있는지"를 알려줍니다.

| 프로토콜 | 번호 |
|---|---|
| ICMP | 1 |
| IGMP | 2 |
| TCP | 6 |
| UDP | 17 |
| OSPF | 89 |

> 포트 번호와 헷갈리지 말 것! 이건 **프로토콜 번호**(IP 헤더), 포트 번호는 TCP/UDP 헤더에 있습니다.

> 💡 시험 포인트: "다음 중 인터넷 계층(또는 전송 계층) 프로토콜이 아닌 것은?" 형태로 소속 계층을 묻는다. **TCP·UDP만 전송 계층**, IP·ICMP·IGMP·ARP·RARP는 인터넷 계층.

---

## 2. ARP / RARP — 주소 변환 프로토콜

### 2-1. 왜 필요한가?

- IP 주소(논리 주소, 32비트)는 "어느 네트워크의 몇 번 호스트인가"를 알려주는 주소.
- MAC 주소(물리 주소, 48비트)는 "랜카드 고유 번호". 같은 LAN 안에서 실제로 프레임을 보낼 땐 **MAC 주소가 있어야** 합니다.
- 그래서 "이 IP 주소 쓰는 사람, MAC 주소 좀 알려줘!"라고 묻는 게 ARP입니다.

### 2-2. ARP (Address Resolution Protocol)

| 항목 | 내용 |
|---|---|
| 기능 | **IP 주소 → MAC 주소** 변환 |
| 요청(ARP Request) | **브로드캐스트** (목적지 MAC = FF:FF:FF:FF:FF:FF) — 누가 가진지 모르니 전체에게 물어봄 |
| 응답(ARP Reply) | **유니캐스트** — 질문한 사람에게만 답함 |
| 결과 저장 | **ARP 캐시(ARP 테이블)**에 일정 시간 저장 → 매번 묻지 않음 |
| 범위 | 같은 네트워크(브로드캐스트 도메인) 안에서만. 다른 네트워크로 갈 땐 **기본 게이트웨이의 MAC**을 ARP로 알아냄 |

**동작 순서 예시** (PC-A 192.168.0.10 → PC-B 192.168.0.20)
1. PC-A가 ARP 캐시를 확인 → 없음
2. "192.168.0.20 누구야? MAC 알려줘" (브로드캐스트)
3. LAN의 모든 호스트가 받지만, 자기 IP가 아니면 무시
4. PC-B만 "나야, 내 MAC은 BB:BB:..." (유니캐스트 응답)
5. PC-A가 캐시에 저장 후 프레임 전송

### 2-3. ARP 관련 용어

| 용어 | 설명 |
|---|---|
| **Gratuitous ARP** | 자기 자신의 IP를 대상으로 보내는 ARP. ① **IP 주소 중복 검사**, ② 내 MAC이 바뀌었음을 주변에 알림(캐시 갱신) |
| **Proxy ARP** | 라우터가 다른 네트워크 호스트 대신 자기 MAC으로 ARP 응답해주는 것 |
| **정적 ARP 항목** | 관리자가 수동으로 IP-MAC 매핑을 고정(`arp -s`) |

### 2-4. RARP (Reverse ARP)

| 항목 | 내용 |
|---|---|
| 기능 | **MAC 주소 → IP 주소** 변환 (ARP의 반대) |
| 사용처 | **디스크가 없는 워크스테이션(Diskless)**이 부팅할 때 자기 IP를 모르니 RARP 서버에 물어봄 |
| 현재 | BOOTP → **DHCP**로 대체되어 거의 쓰이지 않음 |

> 💡 시험 포인트: "ARP 요청은 브로드캐스트, 응답은 유니캐스트", "RARP는 MAC→IP, 디스크 없는 호스트", "Gratuitous ARP = IP 중복 확인".

---

## 3. ICMP / IGMP

### 3-1. ICMP (Internet Control Message Protocol)

**IP는 "보내고 끝"이라 오류가 나도 알려주지 않습니다.** 그래서 "목적지에 못 갔어", "TTL 다 됐어" 같은 **오류 보고와 진단(제어) 메시지**를 담당하는 게 ICMP입니다.

- IP 패킷 안에 담겨 전송됨 (IP 프로토콜 번호 1)
- 오류를 **보고만** 할 뿐, 오류를 **고쳐주지는(재전송하지는) 않음**
- 대표 사용 프로그램: **ping**, **tracert(traceroute)**

#### ICMP 메시지 타입 (시험 단골)

| Type | 이름 | 의미 / 언제 나오나 |
|---|---|---|
| **0** | **Echo Reply** | ping 응답 ("나 살아있어") |
| **3** | **Destination Unreachable** | 목적지 도달 불가 (네트워크·호스트·포트 도달 불가 등) |
| 4 | Source Quench | 송신 속도 줄여라 (현재는 사용 안 함, 폐기됨) |
| **5** | **Redirect** | "더 좋은 경로(게이트웨이)가 있으니 그쪽으로 보내" |
| **8** | **Echo Request** | ping 요청 |
| **11** | **Time Exceeded** | TTL이 0이 되어 폐기됨 (tracert가 이걸 이용) |
| 12 | Parameter Problem | IP 헤더 값 이상 |
| 13 / 14 | Timestamp Request / Reply | 시간 동기 정보 |

> 🧠 외우기: **"0 받고 8 보낸다"** — ping은 **8번(Request)으로 보내고 0번(Reply)으로 받는다**. **3**은 "못 감(Unreachable)", **5**는 "다른 길로(Redirect)", **11**은 "시간(TTL) 초과".

#### ICMP 메시지 분류

| 분류 | 해당 타입 |
|---|---|
| **오류 보고(Error-Reporting)** 메시지 | 3 Destination Unreachable, 4 Source Quench, 5 Redirect, 11 Time Exceeded, 12 Parameter Problem |
| **질의(Query)** 메시지 | 0/8 Echo Reply/Request, 13/14 Timestamp |

### 3-2. tracert(traceroute)의 원리 — ICMP 응용

1. TTL=1로 패킷 전송 → 첫 번째 라우터에서 TTL이 0 → 그 라우터가 **ICMP Time Exceeded(11)** 회신 → "1번째 홉은 이 라우터구나"
2. TTL=2로 전송 → 두 번째 라우터가 Time Exceeded 회신
3. 목적지에 도달할 때까지 TTL을 **1씩 증가**시키며 반복
4. 목적지에 도달하면 Echo Reply(Windows) 또는 Port Unreachable(Linux, UDP 방식)이 돌아오며 종료

> Windows `tracert`는 **ICMP Echo Request**를, Linux `traceroute`는 기본적으로 **UDP(높은 포트 번호)**를 사용합니다.

### 3-3. IGMP (Internet Group Management Protocol)

| 항목 | 내용 |
|---|---|
| 기능 | **멀티캐스트 그룹 가입/탈퇴 관리** — 호스트가 "나 이 멀티캐스트 그룹(예: IPTV 채널) 받을래"를 라우터에 알림 |
| 계층 | 인터넷 계층 (IP 프로토콜 번호 2) |
| 사용 주소 | 클래스 D (224.0.0.0 ~ 239.255.255.255) 멀티캐스트 주소 |
| 메시지 | Membership Query(라우터가 질의), Membership Report(호스트가 가입 보고), Leave Group(v2부터 탈퇴 통보) |
| 활용 | IPTV, 화상회의, 인터넷 방송 등 1:N 전송 |

> 💡 시험 포인트: ICMP 타입 번호 ↔ 이름 짝짓기, "TTL을 1씩 늘리는 명령어 = tracert, 이용 메시지 = Time Exceeded", "멀티캐스트 그룹 관리 = IGMP".

---

## 4. TCP (Transmission Control Protocol)

### 4-1. TCP의 성격

TCP는 **"믿을 수 있는 택배"**입니다. 보내기 전에 연결을 먼저 맺고, 받았는지 확인(ACK)하고, 안 왔으면 다시 보내고, 순서가 뒤바뀌면 맞춰줍니다.

| 특징 | 설명 |
|---|---|
| **연결 지향형** | 데이터 전송 전에 **3-way handshake**로 연결 설정 |
| **신뢰성 보장** | 순서 번호 + 확인 응답(ACK) + **재전송** |
| **흐름 제어** | 받는 쪽이 감당할 수 있는 만큼만 보냄 (**슬라이딩 윈도우**) |
| **혼잡 제어** | 네트워크가 막히면 전송량을 줄임 (Slow Start 등) |
| **전이중(Full-Duplex)** | 양방향 동시 송수신 |
| **바이트 스트림** | 데이터를 바이트 단위 흐름으로 다룸 (순서번호도 바이트 단위) |
| 헤더 크기 | **기본 20바이트** (옵션 포함 최대 60바이트) |

### 4-2. TCP 헤더 구조

```
 0                   15 16                  31 (비트)
+---------------------+---------------------+
|  Source Port (16)   | Destination Port(16)|
+---------------------+---------------------+
|           Sequence Number (32)            |
+-------------------------------------------+
|        Acknowledgment Number (32)         |
+------+------+-------+---------------------+
|HLEN 4|예약  | Flags |   Window Size (16)  |
+------+------+-------+---------------------+
|   Checksum (16)     | Urgent Pointer (16) |
+---------------------+---------------------+
|           Options (가변) + Padding        |
+-------------------------------------------+
```

| 필드 | 크기 | 역할 |
|---|---|---|
| Source / Destination Port | 각 16비트 | 출발지/목적지 **프로그램(서비스)** 구분 |
| **Sequence Number (순서 번호)** | 32비트 | 보내는 데이터의 첫 바이트 번호 → 순서 재조립 |
| **Acknowledgment Number (확인 응답 번호)** | 32비트 | "**다음에 받을 바이트 번호**" (= 여기까지 잘 받았다) |
| **HLEN (헤더 길이, Data Offset)** | 4비트 | 헤더 길이(4바이트 단위) → 5면 20바이트, 15면 60바이트 |
| **Flags (제어 비트)** | 6비트(기본) | URG, ACK, PSH, RST, SYN, FIN |
| **Window Size** | 16비트 | 수신 측이 받을 수 있는 버퍼 크기 → **흐름 제어** |
| **Checksum** | 16비트 | 헤더+데이터 오류 검출 |
| **Urgent Pointer** | 16비트 | URG 플래그가 켜졌을 때 긴급 데이터의 위치 |

> TCP 헤더에는 **TTL·프로토콜 번호·IP 주소가 없습니다**(그건 IP 헤더). "TCP 헤더 필드가 아닌 것" 문제에 TTL이 자주 오답으로 끼어듭니다.

#### TCP 플래그 6개 (URG, ACK, PSH, RST, SYN, FIN)

| 플래그 | 의미 |
|---|---|
| **URG** (Urgent) | 긴급 데이터 있음 → Urgent Pointer 유효 |
| **ACK** (Acknowledgment) | 확인 응답 번호 유효 (연결 후 거의 모든 세그먼트에 켜짐) |
| **PSH** (Push) | 버퍼링하지 말고 즉시 응용 프로그램으로 전달 |
| **RST** (Reset) | **연결을 강제로 끊음(재설정)** — 비정상 상황, 닫힌 포트로 접속 시 |
| **SYN** (Synchronize) | **연결 시작**, 순서 번호 동기화 |
| **FIN** (Finish) | **정상적인 연결 종료** 요청 |

> 🧠 외우기: "**U**nder **A**ttack, **P**lease **R**eset **S**ystem **F**ast" (URG-ACK-PSH-RST-SYN-FIN, 헤더 순서 그대로)

### 4-3. 3-Way Handshake (연결 설정)

```
 클라이언트                      서버
 (CLOSED)                      (LISTEN)
    |  ① SYN (seq=x)              |
    |---------------------------->|  SYN_RCVD
    |  ② SYN + ACK (seq=y, ack=x+1)|
    |<----------------------------|
    |  ③ ACK (ack=y+1)            |
    |---------------------------->|
 ESTABLISHED                 ESTABLISHED
```

1. 클라이언트 → 서버: **SYN** ("연결하자, 내 시작 번호는 x")
2. 서버 → 클라이언트: **SYN + ACK** ("좋아, x+1부터 줘. 내 시작 번호는 y")
3. 클라이언트 → 서버: **ACK** ("y+1부터 줘") → 양쪽 **ESTABLISHED**

> 이 과정을 악용한 공격이 SYN Flooding(07번 보안 노트 참고) — 여기선 "SYN → SYN+ACK → ACK" 순서만 확실히.

### 4-4. 4-Way Handshake (연결 종료)

```
 클라이언트(먼저 종료)              서버
 ESTABLISHED                 ESTABLISHED
    |  ① FIN                       |
    |----------------------------->|  CLOSE_WAIT
 FIN_WAIT_1                        |
    |  ② ACK                       |
    |<-----------------------------|
 FIN_WAIT_2      (서버가 남은 데이터 전송 마무리)
    |  ③ FIN                       |
    |<-----------------------------|  LAST_ACK
    |  ④ ACK                       |
    |----------------------------->|  CLOSED
 TIME_WAIT (2MSL 대기) → CLOSED
```

- 종료는 **FIN → ACK → FIN → ACK** 4단계. (양방향을 **각각** 닫기 때문에 4번)
- **TIME_WAIT**: **먼저 종료를 요청한 쪽(Active Close)**이 마지막 ACK를 보낸 뒤 일정 시간(**2MSL**, MSL=세그먼트 최대 수명) 기다리는 상태.
  - 이유: ① 마지막 ACK가 유실되면 상대가 FIN을 재전송하므로 다시 응답하기 위해, ② 늦게 도착한 이전 연결의 패킷이 새 연결에 섞이지 않게 하기 위해.
- **CLOSE_WAIT**: 상대의 FIN을 받고 **내 쪽 종료를 기다리는** 상태(수동 종료 측).

#### TCP 상태 정리

| 상태 | 의미 |
|---|---|
| LISTEN | 서버가 연결 요청 대기 중 |
| SYN_SENT | 클라이언트가 SYN 보냄 |
| SYN_RCVD | 서버가 SYN 받고 SYN+ACK 보냄 |
| ESTABLISHED | 연결 완료, 데이터 송수신 중 |
| FIN_WAIT_1/2 | 먼저 FIN 보낸 쪽이 대기 |
| CLOSE_WAIT | FIN을 받은 쪽이 애플리케이션 종료 대기 |
| LAST_ACK | 수동 종료 측이 FIN 보내고 마지막 ACK 대기 |
| TIME_WAIT | 능동 종료 측이 2MSL 대기 |
| CLOSED | 연결 없음 |

> `netstat -a` 실행 시 State 열에 이 상태들이 보입니다.

### 4-5. 흐름 제어 (Flow Control) — 슬라이딩 윈도우

- 문제: 보내는 쪽이 너무 빠르면 받는 쪽 버퍼가 넘침.
- 해결: 수신 측이 TCP 헤더의 **Window Size**로 "나 지금 이만큼 더 받을 수 있어"라고 알려주고, 송신 측은 **ACK를 받지 않고도 윈도우 크기만큼 연속 전송**.
- ACK가 오면 윈도우가 **오른쪽으로 미끄러지듯(sliding)** 이동 → "슬라이딩 윈도우".
- 수신 측 버퍼가 꽉 차면 윈도우 0(Zero Window)을 보내 전송 중지.

> 비교: **Stop-and-Wait**는 1개 보내고 ACK 올 때까지 기다림(비효율). 슬라이딩 윈도우는 여러 개를 연속으로 보냄(효율적).

### 4-6. 혼잡 제어 (Congestion Control)

흐름 제어는 "**상대 컴퓨터**가 감당할 수 있나", 혼잡 제어는 "**네트워크(중간 라우터)**가 감당할 수 있나"의 문제입니다. 송신 측은 **혼잡 윈도우(cwnd)**를 따로 관리합니다.

| 기법 | 동작 |
|---|---|
| **Slow Start (느린 시작)** | cwnd를 1 MSS부터 시작해 ACK를 받을 때마다 늘림 → **RTT마다 2배(지수적 증가)**. 임계값(ssthresh)까지 |
| **Congestion Avoidance (혼잡 회피)** | 임계값 도달 후에는 **RTT마다 1씩(선형 증가)** 조심스럽게 증가 |
| **Fast Retransmit (빠른 재전송)** | **중복 ACK 3개**를 받으면 타임아웃을 기다리지 않고 즉시 재전송 |
| **Fast Recovery (빠른 회복)** | 빠른 재전송 후 cwnd를 1로 떨어뜨리지 않고 절반 수준에서 혼잡 회피로 이어감 |

- 타임아웃 발생(심각한 혼잡) → ssthresh를 절반으로, cwnd는 1로 → 다시 Slow Start.
- 이름은 "Slow" Start지만 실제 증가는 **지수적(빠름)**이라는 점이 함정!

> 💡 시험 포인트: 3-way 순서(SYN→SYN/ACK→ACK), RST=강제 종료 vs FIN=정상 종료, TCP 헤더 20바이트, Window Size=흐름 제어, Slow Start=지수 증가, 중복 ACK 3개=빠른 재전송, TIME_WAIT=능동 종료 측.

---

## 5. UDP 와 TCP vs UDP

### 5-1. UDP (User Datagram Protocol)

UDP는 **"일반 우편(엽서)"**입니다. 연결도 안 맺고, 받았는지 확인도 안 하고, 그냥 던집니다. 대신 **빠르고 가볍습니다**.

| 특징 | 설명 |
|---|---|
| **비연결형** | 연결 설정 없이 바로 전송 |
| **비신뢰성** | ACK, 재전송, 순서 보장 **없음** |
| 흐름/혼잡 제어 | **없음** |
| 헤더 | **8바이트 고정**, 필드 **4개** |
| 전송 방식 | 유니캐스트 + **브로드캐스트·멀티캐스트 가능** (TCP는 1:1만) |
| 용도 | 실시간 스트리밍, 음성통화(VoIP), 온라인 게임, DNS 질의, DHCP, SNMP, TFTP, NTP |

#### UDP 헤더 (8바이트)

```
+---------------------+---------------------+
|  Source Port (16)   | Destination Port(16)|
+---------------------+---------------------+
|     Length (16)     |    Checksum (16)    |
+---------------------+---------------------+
```

| 필드 | 설명 |
|---|---|
| Source Port | 출발지 포트 |
| Destination Port | 목적지 포트 |
| **Length** | UDP 헤더 + 데이터 전체 길이 |
| Checksum | 오류 검출 (IPv4에서는 선택 사항) |

> UDP 헤더에는 **순서 번호·확인 응답 번호·윈도우·플래그가 없습니다.**

### 5-2. TCP vs UDP 비교표 (★ 최다 출제)

| 구분 | TCP | UDP |
|---|---|---|
| 연결 방식 | **연결 지향형** (3-way handshake) | **비연결형** |
| 신뢰성 | 높음 (ACK, 재전송, 순서 보장) | 낮음 (보장 안 함) |
| 흐름/혼잡 제어 | 있음 (슬라이딩 윈도우 등) | 없음 |
| 헤더 크기 | **20바이트**(최대 60) | **8바이트** |
| 속도 | 상대적으로 느림 | 빠름 |
| 전송 단위 | 세그먼트(Segment) | 데이터그램(Datagram) |
| 통신 형태 | 1:1 (유니캐스트) | 1:1, 1:N (브로드/멀티캐스트) |
| 대표 서비스 | HTTP, HTTPS, FTP, SMTP, POP3, IMAP, Telnet, SSH | DNS(질의), DHCP, SNMP, TFTP, NTP, 스트리밍, VoIP |

> 💡 시험 포인트: "UDP의 특징으로 옳지 않은 것" → 흐름 제어/재전송/순서 보장 선지가 오답. UDP 헤더 = 4필드 8바이트.

---

## 6. 포트 번호 (★★★ 반드시 암기)

### 6-1. 포트란?

IP 주소가 "건물 주소"라면 포트 번호는 "호수(방 번호)"입니다. 같은 컴퓨터에 웹서버, 메일서버가 같이 있어도 **포트 번호로 어느 프로그램에 줄지** 구분합니다. 16비트 → **0 ~ 65535**.

| 범위 | 이름 | 설명 |
|---|---|---|
| **0 ~ 1023** | **Well-known 포트(잘 알려진 포트)** | 표준 서비스용, IANA가 관리 |
| **1024 ~ 49151** | **Registered 포트(등록된 포트)** | 특정 응용 프로그램용으로 등록 (예: 3306 MySQL, 3389 RDP) |
| **49152 ~ 65535** | **Dynamic / Private 포트(동적 포트)** | 클라이언트가 임시로 사용 (Ephemeral) |

### 6-2. 주요 포트 번호 표

| 포트 | 프로토콜 | 서비스 | 전송 계층 |
|---|---|---|---|
| **20** | FTP-Data | FTP **데이터** 전송 (능동 모드) | TCP |
| **21** | FTP | FTP **제어(명령)** | TCP |
| **22** | SSH | 암호화된 원격 접속 (SFTP, SCP 포함) | TCP |
| **23** | Telnet | 평문 원격 접속 | TCP |
| **25** | SMTP | 메일 **전송** | TCP |
| **53** | DNS | 도메인 이름 변환 | **UDP**(질의) / **TCP**(영역 전송, 큰 응답) |
| **67** | DHCP 서버 (BOOTP) | IP 자동 할당 – 서버 | UDP |
| **68** | DHCP 클라이언트 | IP 자동 할당 – 클라이언트 | UDP |
| **69** | TFTP | 간이 파일 전송 | UDP |
| **80** | HTTP | 웹 | TCP |
| **110** | POP3 | 메일 **수신**(다운로드) | TCP |
| **123** | NTP | 시간 동기화 | UDP |
| **143** | IMAP | 메일 **수신**(서버 보관) | TCP |
| **161** | SNMP | 관리 질의(매니저 → 에이전트) | UDP |
| **162** | SNMP Trap | 이벤트 통보(에이전트 → 매니저) | UDP |
| **389** | LDAP | 디렉터리 서비스 | TCP(주로)/UDP |
| **443** | HTTPS | 보안 웹(HTTP over SSL/TLS) | TCP |
| **445** | SMB (Microsoft-DS) | Windows 파일·프린터 공유 | TCP |
| 465 / 587 | SMTPS / Submission | 보안 메일 전송 | TCP |
| 514 | Syslog | 로그 전송 | UDP |
| 520 | RIP | 라우팅 정보 교환 | UDP |
| 993 | IMAPS | 보안 IMAP | TCP |
| 995 | POP3S | 보안 POP3 | TCP |
| 179 | BGP | 라우팅 정보 교환 | TCP |
| 3306 | MySQL | 데이터베이스 | TCP |
| **3389** | RDP | Windows 원격 데스크톱 | TCP |

> 🧠 외우기:
> - **20·21 FTP, 22 SSH, 23 Telnet, 25 SMTP** → "20대(20~25)는 접속·전송 삼총사"
> - **53 DNS** → "오삼(53)이가 이름을 찾는다"
> - **67/68 DHCP** → 서버가 먼저(67), 클라이언트가 다음(68)
> - **69 TFTP** → FTP(21)의 간이판인데 번호는 훨씬 뒤
> - **110 POP3 / 143 IMAP** → "110(백십)은 POP, 143은 IMAP(아이맵 → 1·4·3)"
> - **161/162 SNMP** → 161 질의, 162 트랩(하나 더 큰 쪽이 '알림')
> - **443 HTTPS** → 80 HTTP의 보안판, "사사삼"
> - **3389 RDP** → 원격 데스크톱

> 💡 시험 포인트: "서비스와 포트 번호의 연결이 옳지 않은 것", "UDP를 사용하는 서비스로만 묶인 것" — **DNS(질의)·DHCP·SNMP·TFTP·NTP는 UDP**, 나머지 대부분 TCP.

---

## 7. 응용 계층 프로토콜 상세

### 7-1. HTTP (HyperText Transfer Protocol, TCP 80)

- 웹 브라우저(클라이언트)와 웹 서버 간 **요청(Request) – 응답(Response)** 프로토콜.
- **무상태(Stateless)**: 서버가 이전 요청을 기억하지 않음 → 그래서 쿠키·세션을 씀.
- HTTPS(443)는 HTTP를 **SSL/TLS로 암호화**한 것.

#### HTTP 메서드

| 메서드 | 역할 |
|---|---|
| **GET** | 자원(페이지) 요청 — 데이터를 URL에 붙여 전송 |
| **POST** | 데이터 전송(폼 제출, 등록) — 본문(Body)에 담음 |
| PUT | 자원 생성/전체 수정 |
| DELETE | 자원 삭제 |
| HEAD | GET과 같지만 **헤더만** 받음 (본문 없음) |
| OPTIONS | 서버가 지원하는 메서드 확인 |
| TRACE | 요청 경로 추적(루프백 테스트) |
| CONNECT | 프록시 터널 연결 |
| PATCH | 자원 일부 수정 |

#### HTTP 상태 코드

| 범위 | 의미 | 대표 코드 |
|---|---|---|
| **1xx** | 정보(처리 중) | 100 Continue |
| **2xx** | **성공** | **200 OK**, 201 Created |
| **3xx** | **리다이렉션(다른 곳으로)** | 301 Moved Permanently, 302 Found, 304 Not Modified |
| **4xx** | **클라이언트 오류** | 400 Bad Request, **401 Unauthorized(인증 필요)**, **403 Forbidden(접근 금지)**, **404 Not Found** |
| **5xx** | **서버 오류** | **500 Internal Server Error**, 502 Bad Gateway, **503 Service Unavailable** |

### 7-2. FTP (File Transfer Protocol, TCP 20/21)

- 파일 송수신. **연결을 2개 사용**: **제어 연결(21번)** + **데이터 연결**.
- 제어 연결은 세션 내내 유지, 데이터 연결은 파일 전송/목록 조회 때마다 생성.
- 계정·비밀번호가 **평문**으로 전송됨 → 보안 대안: **SFTP(SSH 기반, 22)**, **FTPS(SSL/TLS)**.
- **Anonymous FTP**: 계정 없이(anonymous) 접속하는 공개 FTP.

#### 능동(Active) 모드 vs 수동(Passive) 모드

| 구분 | 능동 모드 (Active, PORT) | 수동 모드 (Passive, PASV) |
|---|---|---|
| 제어 연결 | 클라이언트 → 서버 21 | 클라이언트 → 서버 21 |
| **데이터 연결을 누가 맺나** | **서버(20번 포트)**가 클라이언트의 임의 포트로 접속 | **클라이언트**가 서버가 알려준 **임의 포트(1024 이상)**로 접속 |
| 방화벽 문제 | 클라이언트 쪽 방화벽이 서버의 접속을 막을 수 있음 | 클라이언트 방화벽에 유리(바깥으로 나가는 연결만 함) |

> 🧠 외우기: **능동 = 서버가 능동적으로 찾아옴(20번에서)**, **수동 = 서버는 가만히(수동) 기다리고 클라이언트가 찾아감**.

#### FTP 주요 명령(클라이언트)

| 명령 | 의미 |
|---|---|
| `get` / `mget` | 파일 1개 / 여러 개 다운로드 |
| `put` / `mput` | 파일 1개 / 여러 개 업로드 |
| `ascii` / `binary` (`bin`) | 텍스트 / 이진 전송 모드 |
| `ls`, `dir`, `cd`, `pwd` | 목록, 이동, 현재 위치 |
| `bye` / `quit` | 종료 |

### 7-3. TFTP (Trivial FTP, UDP 69)

- FTP의 **간이 버전**: **UDP** 사용, **인증(로그인) 없음**, 디렉터리 목록 조회 기능 없음.
- 용도: 디스크 없는 장비의 부팅 이미지 전송, **라우터·스위치 설정 파일/IOS 백업·복원**.

### 7-4. 이메일 프로토콜 — SMTP / POP3 / IMAP / MIME

```
[보내는 사람 PC] --SMTP--> [보내는 메일서버] --SMTP--> [받는 메일서버] --POP3/IMAP--> [받는 사람 PC]
```

| 프로토콜 | 포트 | 역할 | 특징 |
|---|---|---|---|
| **SMTP** | TCP 25 | 메일 **송신** (클라이언트→서버, 서버→서버) | 원래 7비트 ASCII 텍스트만 지원 |
| **POP3** | TCP 110 | 메일 **수신** | 메일을 PC로 **다운로드**, 기본적으로 서버에서 **삭제** → 한 기기에서 관리 |
| **IMAP** (IMAP4) | TCP 143 | 메일 **수신** | 메일을 **서버에 보관**, 여러 기기에서 **동기화**, 제목만 먼저 보기, 폴더 관리 가능 |
| **MIME** | - | 메일 **확장 형식** | SMTP로 **이미지·음성·동영상·한글 등 비ASCII 데이터**를 보낼 수 있게 인코딩 (Base64 등) |
| S/MIME | - | 보안 MIME | MIME + 암호화·전자서명 |

> 💡 함정: "메일 수신용 프로토콜로 SMTP" → 틀림. SMTP는 **보내기 전용**. 받기는 POP3/IMAP.

### 7-5. DNS (Domain Name System, UDP/TCP 53)

사람은 `www.example.com`을 기억하고, 컴퓨터는 IP 주소로 통신합니다. **도메인 이름 ↔ IP 주소**를 바꿔주는 분산 데이터베이스가 DNS입니다.

#### 도메인 계층 구조

```
                 . (루트)
        /         |          \
      com        net          kr        ← 최상위 도메인(TLD)
       |                       |
    example                    co        ← 2차 도메인
       |                       |
      www (호스트)             naver
```

- FQDN(Fully Qualified Domain Name): `www.example.com.` 처럼 루트까지 전체를 쓴 이름.

#### 질의 방식

| 방식 | 설명 |
|---|---|
| **재귀적 질의 (Recursive)** | 클라이언트 → 로컬 DNS 서버: "**최종 답을 가져다줘**" (DNS 서버가 대신 끝까지 찾아줌) |
| **반복적 질의 (Iterative)** | 로컬 DNS 서버 → 루트 → TLD → 권한 있는 서버 순으로 차례로 물어봄. 각 서버는 "**난 모르지만 저기 물어봐**"(다음 서버 주소)로 응답 |

**동작 순서 (www.example.com 조회)**
1. PC가 **로컬 캐시**와 **hosts 파일** 확인
2. 없으면 로컬 DNS 서버에 **재귀 질의**
3. 로컬 DNS 서버가 루트 서버 → `.com` 서버 → `example.com` 권한 서버 순으로 **반복 질의**
4. 받은 IP를 PC에 응답하고 **캐시에 저장(TTL 동안)**

- **정방향 조회**: 이름 → IP (A, AAAA 레코드)
- **역방향 조회**: IP → 이름 (**PTR 레코드**, `in-addr.arpa` 영역)
- **영역 전송(Zone Transfer)**: 주 DNS → 보조 DNS로 영역 데이터 복사, **TCP 53** 사용

#### DNS 리소스 레코드 (★ 자주 출제)

| 레코드 | 의미 | 예 |
|---|---|---|
| **A** | 도메인 → **IPv4** 주소 | www → 203.0.113.10 |
| **AAAA** | 도메인 → **IPv6** 주소 | www → 2001:db8::10 |
| **CNAME** | **별칭(Alias)** → 정식 이름 | ftp.example.com → www.example.com |
| **MX** | 해당 도메인의 **메일 서버** (우선순위 값 포함, 작을수록 우선) | example.com → 10 mail.example.com |
| **NS** | 해당 영역의 **네임 서버(권한 DNS 서버)** 지정 | example.com → ns1.example.com |
| **PTR** | **IP → 도메인 (역방향)** | 10.113.0.203.in-addr.arpa → www |
| **SOA** | 영역의 **시작 권한 정보**: 주 네임서버, 관리자 메일, 일련번호(Serial), Refresh, Retry, Expire, 최소 TTL | 영역 파일 맨 처음에 1개 |
| TXT | 텍스트 정보 (SPF 등) | |
| SRV | 특정 서비스(예: AD의 LDAP, Kerberos) 위치 | |

> 🧠 외우기: **A**ddress, **AAAA**(A가 4개 = IPv4의 4배인 128비트), **C**anonical **NAME**(별명), **M**ail e**X**changer, **N**ame **S**erver, **P**oin**T**e**R**(역방향), **S**tart **O**f **A**uthority.

### 7-6. DHCP (Dynamic Host Configuration Protocol, UDP 67/68)

PC가 켜질 때 **IP 주소, 서브넷 마스크, 기본 게이트웨이, DNS 서버 주소**를 자동으로 받아오게 해주는 프로토콜. (BOOTP의 발전형)

#### DORA 과정 (★)

| 순서 | 메시지 | 방향 | 전송 방식 |
|---|---|---|---|
| ① | **D**HCP **Discover** | 클라이언트 → 전체 ("DHCP 서버 있어요?") | **브로드캐스트** |
| ② | DHCP **O**ffer | 서버 → 클라이언트 ("이 IP 쓸래?") | 브로드캐스트 또는 유니캐스트 |
| ③ | DHCP **R**equest | 클라이언트 → 전체 ("그 IP 쓸게요" — 여러 서버 중 하나 선택을 알림) | **브로드캐스트** |
| ④ | DHCP **A**ck | 서버 → 클라이언트 ("확정!") | 브로드캐스트 또는 유니캐스트 |

> 🧠 **D-O-R-A** = "도라(Discover-Offer-Request-Ack)". 거절 시 **NAK**, 클라이언트가 주소 반납 시 **Release**, 주소 중복 발견 시 **Decline**.

#### 임대(Lease)

- DHCP 주소는 **임대 기간** 동안만 사용.
- 임대 기간의 **50%(T1)** 경과 시 원래 서버에 갱신 요청(유니캐스트 Request), **87.5%(T2)** 경과 시 아무 서버에게나 재바인딩(브로드캐스트).
- 서버 설정 항목: **범위(Scope)**, **제외 범위**, **예약(Reservation, MAC 주소에 특정 IP 고정)**, 임대 기간, 옵션(게이트웨이·DNS).
- **DHCP 릴레이 에이전트**: DHCP 메시지는 브로드캐스트라 라우터를 못 넘음 → 다른 네트워크의 DHCP 서버로 중계해주는 기능.
- 서버를 못 찾으면 Windows는 **APIPA(169.254.x.x)** 주소를 스스로 할당.

### 7-7. SNMP (Simple Network Management Protocol, UDP 161/162)

네트워크 장비(라우터, 스위치, 서버)의 상태를 **원격으로 감시·관리**하는 프로토콜.

| 구성 요소 | 역할 |
|---|---|
| **SNMP Manager (NMS)** | 관리 시스템. 에이전트에게 정보를 요청하고 설정 |
| **SNMP Agent** | 관리 대상 장비에서 동작. 자신의 정보를 MIB에 유지하고 응답 |
| **MIB (Management Information Base)** | 관리 대상 정보(객체)들의 **데이터베이스**(트리 구조, OID로 식별) |
| SMI | MIB 객체를 정의하는 규칙 |
| **Community** | v1/v2c의 간이 인증 문자열 (기본값 public=읽기, private=쓰기) — **평문** |

#### SNMP 메시지(PDU)

| 메시지 | 방향 | 설명 |
|---|---|---|
| **GetRequest** | 매니저 → 에이전트 | 특정 값 요청 |
| **GetNextRequest** | 매니저 → 에이전트 | 다음 객체 값 요청 (MIB 순회) |
| GetBulkRequest | 매니저 → 에이전트 | 대량 조회 (**v2부터**) |
| **SetRequest** | 매니저 → 에이전트 | 값 **설정(변경)** |
| **GetResponse (Response)** | 에이전트 → 매니저 | 요청에 대한 응답 |
| **Trap** | **에이전트 → 매니저** | 이벤트 발생 시 **요청 없이 비동기 통보** (UDP **162**) |
| InformRequest | 매니저 ↔ 매니저 | 확인 응답을 받는 알림 (v2부터) |

#### 버전 비교

| 버전 | 특징 |
|---|---|
| SNMPv1 | 최초 버전, Community 문자열(평문) 인증 |
| SNMPv2c | GetBulk, Inform 추가, 여전히 Community 기반 |
| **SNMPv3** | **보안 강화: 사용자 인증(USM) + 암호화 + 무결성** |

### 7-8. Telnet vs SSH

| 구분 | Telnet | SSH |
|---|---|---|
| 포트 | TCP **23** | TCP **22** |
| 암호화 | **없음(평문)** → 스니핑에 취약 | **암호화** (공개키 기반 인증 가능) |
| 용도 | 원격 터미널 접속 (구식, 장비 테스트) | 원격 접속, **SFTP, SCP**(파일 전송), 포트 포워딩 |

### 7-9. NTP (Network Time Protocol, UDP 123)

- 네트워크상 컴퓨터들의 **시간을 동기화**.
- 계층 구조(**Stratum**): Stratum 0(원자시계·GPS) → Stratum 1(직접 연결된 서버) → Stratum 2 ... 숫자가 작을수록 정확한 원천에 가까움.
- 로그 분석, 인증(Kerberos 등)에서 시간 일치가 중요.

### 7-10. 기타 알아두면 좋은 응용 프로토콜

| 프로토콜 | 포트 | 설명 |
|---|---|---|
| LDAP | 389 (LDAPS 636) | 디렉터리 서비스 조회 (Active Directory가 사용) |
| SMB/CIFS | 445 | Windows 파일·프린터 공유 |
| RDP | 3389 | Windows 원격 데스크톱 |
| Syslog | UDP 514 | 장비 로그 수집 |

> 💡 시험 포인트: FTP 포트 2개(20 데이터/21 제어)와 능동·수동 차이, POP3 vs IMAP, MIME=멀티미디어 메일, DNS 레코드(MX·PTR·CNAME·SOA), DHCP DORA 순서, SNMP Trap=에이전트가 먼저 알림, SNMPv3=보안.

---

## 8. 라우팅 (Routing)

### 8-1. 라우팅이란?

라우터가 패킷을 받았을 때 **"목적지까지 어느 길(다음 홉)로 보낼지"** 결정하는 것. 그 정보가 담긴 표가 **라우팅 테이블**입니다.

라우팅 테이블에 들어가는 정보: **목적지 네트워크, 서브넷 마스크, 다음 홉(Next Hop) 주소 또는 출구 인터페이스, 메트릭(거리 값), 관리거리**.

### 8-2. 정적 라우팅 vs 동적 라우팅

| 구분 | 정적(Static) 라우팅 | 동적(Dynamic) 라우팅 |
|---|---|---|
| 설정 | 관리자가 **수동으로** 경로 입력 | 라우팅 프로토콜이 **자동으로** 경로 학습 |
| 변화 대응 | 링크 장애 시 자동 우회 **안 됨** | 자동으로 경로 재계산 |
| 부하 | 라우터 CPU·대역폭 부담 적음 | 라우팅 정보 교환으로 부하 발생 |
| 보안 | 경로 정보를 주고받지 않아 상대적으로 안전 | 경로 정보 교환 |
| 적합 | 소규모, 경로가 하나뿐인 **스텁 네트워크** | 대규모, 경로가 자주 바뀌는 네트워크 |
| 예 | `ip route 10.1.1.0 255.255.255.0 192.168.1.1` | RIP, OSPF, EIGRP, BGP |

- **기본 경로(Default Route)**: `0.0.0.0/0` — "모르는 목적지는 전부 여기로". 정적 라우팅의 특수한 형태.

### 8-3. IGP vs EGP

| 구분 | IGP (Interior Gateway Protocol) | EGP (Exterior Gateway Protocol) |
|---|---|---|
| 범위 | **하나의 AS(자율 시스템) 내부** | **AS와 AS 사이** |
| 예 | **RIP, OSPF, EIGRP, IS-IS** (IGRP) | **BGP** |

- **AS (Autonomous System, 자율 시스템)**: 하나의 관리 정책 아래 있는 네트워크 집합 (예: 한 통신사, 한 대기업). AS 번호로 구분.

### 8-4. 거리 벡터 vs 링크 상태 (★)

| 구분 | 거리 벡터 (Distance Vector) | 링크 상태 (Link State) |
|---|---|---|
| 비유 | "**소문**으로 길 찾기" — 이웃이 알려준 거리만 믿음 | "**지도**를 다 그려서 길 찾기" — 전체 토폴로지를 앎 |
| 교환 정보 | **라우팅 테이블 전체**를 **이웃**에게 | **링크 상태 정보(LSA)**를 **전체(영역 내)**에 |
| 업데이트 | **주기적**으로 전체 전송 (RIP 30초) | **변화가 있을 때만** (Triggered) + 가끔 갱신 |
| 알고리즘 | **벨만-포드(Bellman-Ford)** | **다익스트라(Dijkstra) SPF** |
| 수렴 속도 | **느림** | **빠름** |
| 라우팅 루프 | 발생 가능 (Count to Infinity) | 거의 없음 |
| 자원 사용 | CPU·메모리 적게 | CPU·메모리 많이 |
| 프로토콜 | **RIP**, IGRP | **OSPF, IS-IS** |

- **하이브리드(Advanced Distance Vector)**: **EIGRP** — 거리벡터 기반이지만 링크상태 장점(변화 시 부분 업데이트, 빠른 수렴) 결합.
- **경로 벡터(Path Vector)**: **BGP** — 경유하는 AS 경로 목록을 보고 결정.

### 8-5. 라우팅 프로토콜별 정리

#### RIP (Routing Information Protocol)

| 항목 | 내용 |
|---|---|
| 유형 | **거리 벡터**, IGP |
| 메트릭 | **홉 수(Hop Count)** — 거쳐가는 라우터 개수만 봄 (속도 무시) |
| **최대 홉** | **15** (16 = 도달 불가, 무한대) → **소규모 네트워크용** |
| 업데이트 | **30초마다** 라우팅 테이블 전체를 이웃에 전송 |
| 타이머 | Invalid 180초, Hold-down 180초, Flush 240초 |
| 전송 | **UDP 520** |
| 알고리즘 | 벨만-포드 |

| 구분 | RIPv1 | RIPv2 |
|---|---|---|
| 주소 방식 | **클래스풀(Classful)** — 서브넷 마스크 정보 미포함 | **클래스리스(Classless)** — 서브넷 마스크 포함, **VLSM·CIDR 지원** |
| 업데이트 전송 | **브로드캐스트**(255.255.255.255) | **멀티캐스트(224.0.0.9)** |
| 인증 | 없음 | **인증 지원**(평문/MD5) |

#### OSPF (Open Shortest Path First)

| 항목 | 내용 |
|---|---|
| 유형 | **링크 상태**, IGP, **개방형 표준**(어느 제조사든 사용) |
| 알고리즘 | **다익스트라 SPF(최단 경로 우선)** |
| 메트릭 | **코스트(Cost)** = 기준 대역폭(10^8) ÷ 인터페이스 대역폭 → **대역폭이 클수록 코스트 작음** |
| 홉 제한 | 없음 → **대규모 네트워크 적합** |
| 영역(Area) | 네트워크를 Area로 나눠 계층적으로 관리. **Area 0 = 백본(Backbone) 영역**, 다른 Area는 반드시 Area 0과 연결 |
| 업데이트 | 변화가 있을 때 **LSA(Link State Advertisement)** 전송 → 각 라우터가 **LSDB** 구성 후 SPF 계산 |
| 이웃 관리 | **Hello 패킷**으로 이웃 발견·유지 |
| 전송 | IP 프로토콜 번호 **89** (TCP/UDP 아님), 멀티캐스트 224.0.0.5(전체 OSPF 라우터), 224.0.0.6(DR/BDR) |
| 기타 | VLSM·CIDR 지원, 인증 지원, 멀티 액세스 망에서 **DR/BDR** 선출 |

#### EIGRP (Enhanced Interior Gateway Routing Protocol)

| 항목 | 내용 |
|---|---|
| 유형 | **하이브리드(고급 거리 벡터)**, IGP |
| 개발 | **시스코(Cisco)** 개발 (IGRP의 개선판) |
| 알고리즘 | **DUAL**(Diffusing Update Algorithm) → 빠른 수렴, 루프 없는 백업 경로 |
| 메트릭 | **대역폭, 지연**(기본) + 신뢰성, 부하 (복합 메트릭) |
| 업데이트 | 변화 시 **부분(Partial) 업데이트** |
| 기타 | **비동일 비용 로드 밸런싱** 가능, VLSM 지원 |

#### IS-IS (Intermediate System to Intermediate System)

- **링크 상태**, IGP. 원래 **OSI 표준**용으로 만들어짐.
- 다익스트라 알고리즘 사용, 대형 통신사(ISP) 백본에서 사용.
- IP 위가 아니라 **데이터링크 계층 위에서 직접** 동작.

#### BGP (Border Gateway Protocol)

| 항목 | 내용 |
|---|---|
| 유형 | **EGP**, **경로 벡터(Path Vector)** |
| 용도 | **AS와 AS 사이** 라우팅 → **인터넷의 핵심 라우팅 프로토콜** (ISP 간) |
| 전송 | **TCP 179** (신뢰성 있는 연결 사용) |
| 종류 | **eBGP**(서로 다른 AS 간), **iBGP**(같은 AS 내부 BGP 라우터 간) |
| 경로 결정 | AS_PATH 등 다양한 **속성(Attribute)**과 정책 기반 |

### 8-6. 관리 거리 (AD, Administrative Distance)

**같은 목적지를 여러 라우팅 프로토콜로 알게 됐을 때, 어떤 정보를 믿을지** 정하는 신뢰도 값. **작을수록 우선(신뢰도 높음)**. (시스코 기준 대표값)

| 경로 출처 | AD |
|---|---|
| **직접 연결(Connected)** | **0** |
| **정적 경로(Static)** | **1** |
| eBGP | 20 |
| **EIGRP** (내부) | **90** |
| IGRP | 100 |
| **OSPF** | **110** |
| IS-IS | 115 |
| **RIP** | **120** |
| EIGRP (외부) | 170 |
| iBGP | 200 |
| 알 수 없음(사용 안 함) | 255 |

> 🧠 외우기: **"직0 정1 이(eBGP)20, 이(EIGRP)구(90), 오(OSPF)110, 립(RIP)120"**. 숫자가 작을수록 우선!
> - **메트릭**: 같은 프로토콜 안에서 경로끼리 비교 (홉 수, 코스트 등)
> - **관리 거리**: 서로 다른 프로토콜끼리 비교

### 8-7. 라우팅 루프와 방지 기법 (거리 벡터의 약점)

**라우팅 루프**: 잘못된 경로 정보 때문에 패킷이 라우터 사이를 뱅뱅 도는 현상. 거리 벡터에서는 거리가 1씩 계속 늘어나는 **무한 카운팅(Count to Infinity)** 문제가 생깁니다. (IP 헤더의 TTL이 0이 되면 결국 폐기되긴 함)

| 기법 | 설명 |
|---|---|
| **최대 홉 수 제한** | RIP은 16을 무한대로 간주 → 무한 카운팅을 16에서 멈춤 |
| **Split Horizon (스플릿 호라이즌)** | 어떤 경로를 **학습한 인터페이스로는 그 경로를 다시 광고하지 않음** ("들은 데로 되돌려 말하지 않기") |
| **Route Poisoning (경로 포이즈닝)** | 끊긴 경로를 **메트릭 무한대(RIP 16)**로 광고해 "이 길 죽었음"을 즉시 알림 |
| **Poison Reverse (포이즌 리버스)** | 포이즈닝 정보를 받은 라우터가 받은 쪽으로 다시 무한대로 응답 (Split Horizon 예외) |
| **Hold-down Timer (홀드다운 타이머)** | 경로가 다운됐다는 정보를 받으면 **일정 시간 동안 그 경로에 대한 (더 나쁜) 갱신을 무시** → 잘못된 정보 확산 방지 |
| **Triggered Update (트리거 업데이트)** | 30초를 기다리지 않고 **변화 즉시** 업데이트 전송 |

> 💡 시험 포인트: RIP=홉 15/30초/거리벡터/벨만-포드, OSPF=링크상태/다익스트라/코스트/Area 0, BGP=AS 간/EGP/TCP 179, EIGRP=시스코/하이브리드/DUAL, AD 작을수록 우선, Split Horizon 정의.

---

## 9. 네트워크 진단 명령어

### 9-1. ping

- **ICMP Echo Request(8) / Echo Reply(0)**로 상대 호스트의 **연결 가능 여부·응답 시간(RTT)·TTL** 확인.
- 결과 예: `Reply from 8.8.8.8: bytes=32 time=30ms TTL=117`

| 옵션 (Windows) | 의미 |
|---|---|
| `-t` | 중지(Ctrl+C)할 때까지 **계속** ping |
| `-n 횟수` | 보낼 횟수 (기본 4회) |
| `-l 크기` | 보낼 데이터 크기 |
| `-a` | IP 주소를 호스트 이름으로 확인 |
| `-i TTL` | TTL 값 지정 |

> Linux ping은 기본적으로 **무한 반복**, `-c 횟수`로 횟수 지정.

### 9-2. tracert (Windows) / traceroute (Linux)

- 목적지까지 **거쳐가는 라우터(홉) 경로와 각 구간 지연 시간** 표시.
- 원리: **TTL을 1부터 1씩 증가** → 각 라우터가 **ICMP Time Exceeded** 응답 (3-2절 참고).
- 응답 없는 구간은 `* * *`(요청 시간 초과)로 표시.
- `tracert -d`: IP 주소를 이름으로 변환하지 않음(빠름).

### 9-3. pathping (Windows)

- **ping + tracert를 합친** 명령. 경로를 찾은 뒤 각 홉에 여러 번 패킷을 보내 **구간별 패킷 손실률(%)**까지 통계로 보여줌.

### 9-4. netstat

현재 **네트워크 연결 상태, 열린(LISTEN) 포트, 라우팅 테이블, 프로토콜 통계** 확인.

| 옵션 | 의미 |
|---|---|
| **`-a`** | **모든 연결과 수신 대기(LISTENING) 포트** 표시 |
| **`-n`** | 주소·포트를 **숫자 형식**으로 표시 (DNS 변환 안 함 → 빠름) |
| **`-r`** | **라우팅 테이블** 표시 (`route print`와 동일) |
| **`-s`** | **프로토콜별 통계**(IP, ICMP, TCP, UDP) |
| `-e` | 이더넷 통계(송수신 바이트 등) |
| `-o` | 각 연결의 **프로세스 ID(PID)** 표시 (Windows) |
| `-p 프로토콜` | 특정 프로토콜(TCP/UDP)만 표시 |

> 자주 쓰는 조합: `netstat -an` (모든 연결을 숫자로), `netstat -ano` (+PID → 어떤 프로그램이 포트를 쓰는지 확인)

### 9-5. nslookup

- **DNS 서버에 직접 질의**하여 도메인 ↔ IP 확인, DNS 문제 진단.
- 예: `nslookup www.example.com`, `nslookup 8.8.8.8`(역방향)
- 대화형 모드에서 `set type=MX` → 메일 서버 레코드 조회, `set type=NS`, `server 8.8.8.8`(질의할 DNS 서버 변경)
- Linux에서는 `dig`, `host` 명령도 사용.

### 9-6. ipconfig (Windows)

| 명령 | 의미 |
|---|---|
| `ipconfig` | IP 주소, 서브넷 마스크, 기본 게이트웨이 요약 |
| **`ipconfig /all`** | **상세 정보**: MAC(물리적 주소), DHCP 사용 여부, DHCP 서버, DNS 서버, 임대 시간 등 |
| **`ipconfig /release`** | DHCP로 받은 IP **반납** |
| **`ipconfig /renew`** | DHCP로 IP **재발급(갱신)** |
| **`ipconfig /flushdns`** | **DNS 확인자 캐시 삭제** (DNS 변경 반영 안 될 때) |
| **`ipconfig /displaydns`** | **DNS 캐시 내용 보기** |
| `ipconfig /registerdns` | DHCP 갱신 및 DNS 이름 재등록 |

> Linux는 `ifconfig` 또는 `ip addr`(05번 리눅스 노트 참고).

### 9-7. arp

| 명령 | 의미 |
|---|---|
| **`arp -a`** | **ARP 캐시(IP ↔ MAC 매핑 테이블) 보기** |
| `arp -d IP` | ARP 캐시 항목 삭제 |
| `arp -s IP MAC` | **정적 ARP 항목 추가** (ARP 스푸핑 대응용) |

### 9-8. route

| 명령 | 의미 |
|---|---|
| **`route print`** | **라우팅 테이블 보기** (= `netstat -r`) |
| `route add 목적지 mask 마스크 게이트웨이` | 경로 추가 (`-p` 붙이면 재부팅 후에도 유지) |
| `route delete 목적지` | 경로 삭제 |

### 9-9. 명령어 한눈에 보기

| 하고 싶은 일 | 명령 |
|---|---|
| 상대가 살아있는지 | `ping` |
| 어디서 막히는지(경로) | `tracert` / `traceroute` |
| 구간별 손실률 | `pathping` |
| 열린 포트·연결 상태 | `netstat -an` |
| 라우팅 테이블 | `route print` / `netstat -r` |
| DNS 질의 | `nslookup` |
| 내 IP·MAC·DNS 서버 | `ipconfig /all` |
| DNS 캐시 비우기 | `ipconfig /flushdns` |
| IP 다시 받기 | `ipconfig /release` → `ipconfig /renew` |
| IP-MAC 매핑 확인 | `arp -a` |

> 💡 시험 포인트: "라우팅 테이블을 보는 명령(옵션)", "DNS 캐시 삭제", "모든 연결·LISTEN 포트 확인", "TTL을 증가시키며 경로 추적" — 명령어와 옵션을 정확히 매칭.

---

## ★ 핵심사항 (시험 직전 10분 암기용)

- 전송 계층 = **TCP, UDP** / 인터넷 계층 = **IP, ICMP, IGMP, ARP, RARP**
- **ARP: IP→MAC**, 요청 **브로드캐스트**, 응답 **유니캐스트**, 결과는 ARP 캐시
- **RARP: MAC→IP**, 디스크 없는 워크스테이션 / Gratuitous ARP = **IP 중복 확인**
- ICMP: **0 Echo Reply, 3 목적지 도달 불가, 5 Redirect, 8 Echo Request, 11 Time Exceeded**
- ICMP는 오류를 **보고만** 하고 재전송하지 않음 / ping·tracert가 ICMP 사용
- **IGMP = 멀티캐스트 그룹 가입·탈퇴 관리**
- TCP = 연결지향·신뢰성·흐름/혼잡 제어, 헤더 **20바이트**(최대 60)
- TCP 플래그: **URG ACK PSH RST SYN FIN** / **RST=강제 종료, FIN=정상 종료**
- 3-way: **SYN → SYN+ACK → ACK** / 종료 4-way: **FIN → ACK → FIN → ACK**
- **TIME_WAIT = 먼저 끊은 쪽**이 2MSL 대기
- 흐름 제어 = **슬라이딩 윈도우(Window 필드)** / 혼잡 제어 = **Slow Start(지수)→혼잡 회피(선형)**, **중복 ACK 3개 → 빠른 재전송**
- UDP = 비연결, 헤더 **8바이트 4필드**(출발 포트, 목적 포트, 길이, 체크섬)
- 포트: Well-known **0~1023**, 등록 1024~49151, 동적 49152~65535
- **20/21 FTP, 22 SSH, 23 Telnet, 25 SMTP, 53 DNS, 67/68 DHCP, 69 TFTP, 80 HTTP, 110 POP3, 123 NTP, 143 IMAP, 161/162 SNMP, 389 LDAP, 443 HTTPS, 445 SMB, 3389 RDP**
- UDP 서비스: **DNS(질의), DHCP, TFTP, SNMP, NTP**
- FTP **능동 = 서버가 20번에서 접속**, **수동 = 클라이언트가 서버 임의 포트로 접속**
- **SMTP=보내기, POP3=받아서 삭제(다운로드), IMAP=서버 보관·동기화, MIME=멀티미디어 메일**
- DNS 레코드: **A(IPv4) AAAA(IPv6) CNAME(별칭) MX(메일) NS(네임서버) PTR(역방향) SOA(영역 시작 권한)**
- DNS 영역 전송 = **TCP 53**
- DHCP = **DORA**(Discover-Offer-Request-Ack), Discover·Request는 브로드캐스트, 임대 50%에서 갱신
- SNMP: Manager / Agent / **MIB**, **Trap = 에이전트가 매니저에 비동기 통보(162)**, **v3 = 인증·암호화**
- RIP: **거리벡터, 홉 수, 최대 15홉, 30초**, 벨만-포드, UDP 520, v2는 VLSM·멀티캐스트·인증
- OSPF: **링크상태, 다익스트라, 코스트(대역폭), Area 0 백본**, 대규모, IP 89
- EIGRP: **시스코, 하이브리드, DUAL** / IS-IS: 링크상태, OSI / **BGP: AS 간(EGP), 경로 벡터, TCP 179**
- AD: **직접 0, 정적 1, EIGRP 90, OSPF 110, RIP 120** → 작을수록 우선
- 루프 방지: **Split Horizon(받은 쪽으로 광고 안 함)**, Route Poisoning(무한대 16 광고), Hold-down(일정 시간 갱신 무시)
- `netstat -a`(전체+LISTEN) `-n`(숫자) **`-r`(라우팅 테이블)** `-s`(통계) / `route print`
- `ipconfig /all /release /renew` **`/flushdns`(캐시 삭제)** `/displaydns`(캐시 보기) / `arp -a`

---

## ⚠️ 헷갈리는 함정 포인트

| 헷갈리는 쌍 | 구분법 |
|---|---|
| ARP vs RARP | ARP: **IP→MAC** / RARP: **MAC→IP** (R=Reverse) |
| ARP 요청 vs 응답 | 요청 = **브로드캐스트** / 응답 = **유니캐스트** |
| ICMP 0 vs 8 | **8 = Request(보냄)**, **0 = Reply(받음)** |
| ICMP 3 vs 11 | 3 = 목적지 **도달 불가** / 11 = **TTL 초과**(tracert) |
| ICMP vs IGMP | ICMP = 오류·진단 / IGMP = **멀티캐스트 그룹 관리** |
| RST vs FIN | RST = **강제(비정상)** 종료 / FIN = **정상** 종료 |
| TIME_WAIT vs CLOSE_WAIT | TIME_WAIT = **먼저 끊은(능동)** 쪽 / CLOSE_WAIT = **FIN 받은(수동)** 쪽 |
| 흐름 제어 vs 혼잡 제어 | 흐름 = **수신자 버퍼** 보호(Window) / 혼잡 = **네트워크** 보호(cwnd) |
| Slow Start | 이름과 달리 **지수적 증가** (혼잡 회피가 선형) |
| TCP 헤더 vs UDP 헤더 | 20바이트 vs **8바이트**, UDP에는 순서번호·ACK·윈도우 **없음** |
| 프로토콜 번호 vs 포트 번호 | TCP 6 / UDP 17 / ICMP 1 (IP 헤더) ↔ 80, 443 등(TCP/UDP 헤더) |
| FTP 20 vs 21 | **21 = 제어(명령)**, **20 = 데이터** |
| FTP 능동 vs 수동 | 데이터 연결을 **서버가** 맺으면 능동, **클라이언트가** 맺으면 수동 |
| FTP vs TFTP | FTP: TCP 20/21, 인증 有 / TFTP: **UDP 69, 인증 無** |
| POP3 vs IMAP | POP3(110): 다운로드 후 **삭제** / IMAP(143): **서버 보관·동기화** |
| SMTP | **보내기 전용** (받기 아님!) |
| SNMP 161 vs 162 | 161 = 매니저의 Get/Set **질의** / 162 = 에이전트의 **Trap** |
| DNS UDP vs TCP | 일반 질의 = **UDP 53** / 영역 전송 = **TCP 53** |
| A vs AAAA vs PTR | A = IPv4, AAAA = IPv6, PTR = **IP→이름(역방향)** |
| CNAME vs NS vs MX | CNAME = 별칭 / NS = 네임서버 / MX = 메일서버 |
| 재귀 vs 반복 질의 | 재귀 = "**최종 답** 가져와" (클라이언트→로컬 DNS) / 반복 = "**다음 서버** 알려줘" (로컬 DNS→루트·TLD) |
| 거리 벡터 vs 링크 상태 | 거리벡터: 이웃에게 **전체 테이블 주기적**, 벨만-포드, RIP / 링크상태: **변화 시 LSA**, 다익스트라, OSPF |
| IGP vs EGP | IGP: AS **내부**(RIP, OSPF, EIGRP, IS-IS) / EGP: AS **간**(BGP) |
| 메트릭 vs 관리거리 | 메트릭 = 같은 프로토콜 내 경로 비교 / AD = **다른 프로토콜 간** 비교 |
| RIP 최대 홉 | **15** (16은 도달 불가) |
| Split Horizon vs Route Poisoning | Split Horizon = **받은 쪽으로 안 보냄** / Poisoning = **무한대 값으로 보냄** |
| netstat -r vs -s | **-r = 라우팅(Route)**, **-s = 통계(Statistics)** |
| ipconfig /flushdns vs /displaydns | flush = **삭제**, display = **보기** |

---

## 🧠 암기 팁

- **인터넷 계층 5형제**: "**아이(IP)가 아(ARP)라(RARP) 이(ICMP)그(IGMP)**" → IP, ARP, RARP, ICMP, IGMP
- **ICMP 타입**: "**영(0)이 답하고 팔(8)이 묻는다, 삼(3) 못 가고 오(5) 돌아가고 십일(11) 시간 끝**"
- **TCP 플래그 순서**: "**U**nder **A**ttack, **P**lease **R**eset **S**ystem **F**ast" (URG ACK PSH RST SYN FIN)
- **3-way**: "**신(SYN)청 → 신청확인(SYN+ACK) → 확인(ACK)**"
- **DHCP**: "**도라(DORA)에몽이 IP를 준다**" — Discover, Offer, Request, Ack
- **UDP 서비스**: "**D**NS, **D**HCP, **T**FTP, **S**NMP, **N**TP" → "**디디 티에스엔**(DD TSN)"
- **포트 20번대**: 20-21 FTP, 22 SSH, 23 Telnet, 25 SMTP → "**에프·에프·에스·텔·메일**"
- **메일**: "**S**MTP = **S**end, **P**OP3 = **P**ull(가져와서 지움), **IMAP** = **I**n **MA**il server **P**reserve(서버에 보관)"
- **DNS 레코드**: "**M**X = **M**ail, **P**TR = **P**oint back(역방향), **C**NAME = **C**all name(별명)"
- **SNMP**: "**Trap은 덫** — 장비가 먼저 '걸렸다!' 하고 알림"
- **라우팅**: "**RIP은 홉수 세는 동네 소문(거리벡터)**, **OSPF는 전체 지도 펼친 다익스트라(링크상태)**, **BGP는 나라(AS) 사이 국경(Border)**"
- **AD 값**: "**0 직결, 1 정적, 90 EIGRP, 110 OSPF, 120 RIP**" → "**공·일·구공·백십·백이십**"
- **netstat**: "**a**ll, **n**umber, **r**oute, **s**tatistics"

---

## 📝 연습문제 (과거 기출 유형 변형, 25문항)

**[프로토콜-01]** TCP/IP 4계층 모델에서 **네트워크 인터페이스(링크) 계층**에 해당하는 것은?

① ICMP
② TCP
③ HTTP
④ 이더넷(Ethernet)

---

**[프로토콜-02]** 라우터가 패킷을 받아 보니 송신 호스트와 같은 네트워크에 목적지로 가는 **더 나은 다음 홉 라우터**가 있을 때, 송신 호스트에게 경로를 바꾸라고 알려 주는 ICMP 메시지는?

① Echo Reply
② Source Quench
③ Redirect
④ Parameter Problem

---

**[프로토콜-03]** 하드 디스크가 없는 워크스테이션이 부팅할 때 자신의 MAC 주소는 알지만 IP 주소를 모르는 경우, 서버에 자신의 IP 주소를 요청하기 위해 사용하는 프로토콜은?

① ARP
② RARP
③ IGMP
④ ICMP

---

**[프로토콜-04]** ICMP 메시지 중 **오류 보고(Error-Reporting)** 메시지에 해당하지 **않는** 것은?

① Destination Unreachable
② Time Exceeded
③ Echo Request
④ Parameter Problem

---

**[프로토콜-05]** 경로 추적 명령어(tracert/traceroute)는 TTL 값을 1부터 하나씩 증가시키면서 패킷을 전송한다. 이때 TTL이 0이 된 패킷을 폐기한 중간 라우터가 송신 측에 돌려보내는 ICMP 메시지는?

① Echo Reply
② Time Exceeded
③ Redirect
④ Source Quench

---

**[프로토콜-06]** RIPv2가 RIPv1과 비교하여 추가·개선된 특징이 **아닌** 것은?

① 라우팅 업데이트에 서브넷 마스크 정보를 포함하여 VLSM(클래스리스)을 지원한다.
② 업데이트를 브로드캐스트 대신 멀티캐스트(224.0.0.9)로 전송한다.
③ 최대 홉 수를 255로 확장하여 대규모 네트워크를 지원한다.
④ 라우팅 업데이트에 대한 인증 기능을 지원한다.

---

**[프로토콜-07]** TCP 헤더에서 URG 플래그가 1일 때 함께 사용되어, 세그먼트 안에서 **긴급 데이터가 끝나는 위치**를 알려 주는 필드는?

① Urgent Pointer
② Window
③ Checksum
④ Data Offset

---

**[프로토콜-08]** 클라이언트가 순서 번호(Sequence Number) **1000**으로 SYN 세그먼트를 보냈다. 서버가 응답으로 보내는 SYN+ACK 세그먼트의 확인 응답 번호(Acknowledgment Number)는?

① 999
② 1000
③ 0
④ 1001

---

**[프로토콜-09]** Windows 명령 프롬프트에서 **DNS 서버에 직접 질의**하여 도메인 이름에 대한 IP 주소나 MX·NS 같은 레코드 정보를 확인하는 명령어는?

① tracert
② nslookup
③ arp -a
④ netstat -n

---

**[프로토콜-10]** UDP 헤더의 **Length** 필드가 나타내는 값으로 옳은 것은?

① UDP 데이터(페이로드)만의 길이
② IP 헤더를 포함한 전체 패킷의 길이
③ UDP 헤더만의 길이
④ UDP 헤더와 데이터를 합한 UDP 데이터그램 전체 길이

---

**[프로토콜-11]** TCP 연결을 설정할 때 서로 알려 주며, **하나의 TCP 세그먼트에 담을 수 있는 최대 데이터(페이로드) 크기**를 의미하는 값은?

① MTU
② MSS
③ RTT
④ TTL

---

**[프로토콜-12]** TCP 혼잡 제어에서 연결 초기에 혼잡 윈도우(cwnd)를 작은 값에서 시작하여 ACK를 받을 때마다 늘려, 결과적으로 RTT마다 약 2배씩 지수적으로 증가시키는 단계는?

① Slow Start
② Congestion Avoidance
③ Fast Retransmit
④ Stop-and-Wait

---

**[프로토콜-13]** Windows 명령 프롬프트에서 IP 주소와 MAC 주소의 대응 정보가 저장된 **ARP 캐시 테이블**을 확인하는 명령어는?

① netstat -r
② route print
③ ipconfig /all
④ arp -a

---

**[프로토콜-14]** IANA가 표준 서비스용으로 할당한 잘 알려진 포트(Well-known Port)의 범위로 옳은 것은?

① 0 ~ 255
② 0 ~ 511
③ 0 ~ 1023
④ 1024 ~ 49151

---

**[프로토콜-15]** 서비스와 기본 포트 번호의 연결이 옳지 **않은** 것은?

① POP3 – 143
② SSH – 22
③ SMTP – 25
④ HTTPS – 443

---

**[프로토콜-16]** DNS는 일반적인 이름 질의·응답에 UDP 53번을 사용한다. DNS가 **TCP 53번**을 사용하는 대표적인 경우는?

① 클라이언트가 자신의 DNS 캐시를 조회할 때
② 주 DNS 서버와 보조 DNS 서버 간의 영역 전송(Zone Transfer)
③ DNS 서버가 루트 힌트 파일을 읽어 들일 때
④ 역방향(PTR) 조회를 할 때

---

**[프로토콜-17]** NTP의 계층(Stratum) 구조에서 원자시계·GPS 수신기처럼 **기준 시각을 만들어 내는 시계 장치 자체**에 해당하는 계층은?

① Stratum 0
② Stratum 1
③ Stratum 15
④ Stratum 16

---

**[프로토콜-18]** HTTP 응답 상태 코드의 범주 중 **3xx**(예: 301, 302)가 의미하는 것은?

① 요청 성공
② 클라이언트 오류
③ 리다이렉션(다른 위치로 이동)
④ 서버 오류

---

**[프로토콜-19]** DNS 리소스 레코드 중 해당 도메인으로 오는 전자우편을 처리할 메일 서버를 지정하는 레코드는?

① MX
② CNAME
③ A
④ PTR

---

**[프로토콜-20]** DHCP 클라이언트가 IP 주소를 할당받는 과정을 순서대로 바르게 나열한 것은?

① Request → Offer → Discover → Ack
② Discover → Request → Offer → Ack
③ Offer → Discover → Ack → Request
④ Discover → Offer → Request → Ack

---

**[프로토콜-21]** SNMP 메시지 중 **매니저(Manager)가 에이전트(Agent)의 MIB 객체 값을 변경**하기 위해 보내는 메시지는?

① GetRequest
② GetNextRequest
③ SetRequest
④ Trap

---

**[프로토콜-22]** RIP(Routing Information Protocol)에 대한 설명으로 옳지 **않은** 것은?

① 거리 벡터(Distance Vector) 방식의 라우팅 프로토콜이다.
② 최대 홉 수는 15이며, 16은 도달할 수 없는 네트워크로 간주한다.
③ 기본적으로 30초마다 라우팅 테이블 정보를 이웃 라우터에게 전송한다.
④ 다익스트라(Dijkstra) 알고리즘으로 전체 토폴로지 기반의 최단 경로를 계산한다.

---

**[프로토콜-23]** OSI 표준으로 만들어진 **링크 상태** 라우팅 프로토콜로, 대형 ISP 백본망에서 OSPF와 함께 많이 쓰이는 IGP는?

① EIGRP
② IS-IS
③ RIP
④ EGP

---

**[프로토콜-24]** 하나의 라우터가 동일한 목적지 네트워크에 대한 경로를 RIP, OSPF, EIGRP로 각각 학습했고, 관리자가 같은 목적지로 정적 경로도 설정하였다. 기본 관리 거리(AD) 값을 기준으로 할 때 라우팅 테이블에 최종 등록되는 경로의 출처는? (시스코 라우터 기준)

① RIP
② OSPF
③ EIGRP
④ 정적 경로(Static Route)

---

**[프로토콜-25]** 거리 벡터 라우팅에서 라우팅 루프를 방지하기 위해, 어떤 경로 정보를 학습한 인터페이스로는 그 경로 정보를 다시 광고하지 않는 기법은?

① Split Horizon
② Hold-down Timer
③ Route Poisoning
④ Triggered Update

---

## ✅ 정답 및 해설

| 문항 | 정답 | 해설 |
|---|---|---|
| 프로토콜-01 | ④ | 네트워크 인터페이스 계층 = OSI 1·2계층 = **이더넷**, Wi-Fi, PPP 등. ICMP는 인터넷 계층, TCP는 전송 계층, HTTP는 응용 계층. |
| 프로토콜-02 | ③ | **Redirect(Type 5)** = 더 좋은 경로(게이트웨이) 안내. Echo Reply는 ping 응답, Source Quench는 송신 속도를 낮추라는(현재는 폐기된) 메시지, Parameter Problem은 헤더 값 오류 보고. |
| 프로토콜-03 | ② | **RARP = MAC→IP**, 디스크 없는(Diskless) 워크스테이션용. ARP는 IP→MAC, IGMP는 멀티캐스트 그룹 관리, ICMP는 오류·제어 메시지. |
| 프로토콜-04 | ③ | ICMP 메시지는 **오류 보고**(Destination Unreachable, Time Exceeded, Parameter Problem, Redirect 등)와 **질의**(Echo Request/Reply, Timestamp 등)로 나뉜다. Echo Request는 ping이 보내는 **질의** 메시지. |
| 프로토콜-05 | ② | TTL이 0이 되어 폐기되면 라우터가 **ICMP Time Exceeded(Type 11)**를 회신 → tracert는 이것으로 각 홉을 알아낸다. Echo Reply는 목적지 응답, Redirect는 더 나은 경로 안내, Source Quench는 폐기된 흐름 제어 메시지. |
| 프로토콜-06 | ③ | RIPv2도 **최대 홉 수는 15**(16 = 도달 불가)로 RIPv1과 같다. ①(서브넷 마스크 전달·VLSM), ②(224.0.0.9 멀티캐스트), ④(인증)는 RIPv2에서 추가된 기능. |
| 프로토콜-07 | ① | **Urgent Pointer** = 긴급 데이터의 끝 위치(URG=1일 때만 유효). Window는 흐름 제어용 수신 윈도우, Checksum은 오류 검출, Data Offset은 TCP 헤더 길이(4바이트 단위). |
| 프로토콜-08 | ④ | ACK 번호 = **다음에 받기를 기대하는 순서 번호**. SYN은 데이터가 없어도 순서 번호 1개를 소비하므로 1000 + 1 = **1001**. |
| 프로토콜-09 | ② | **nslookup** = DNS 질의 도구(`set type=mx` 등으로 레코드 지정 가능). tracert는 경로 추적, arp -a는 ARP 캐시, netstat -n은 연결 상태를 숫자 주소로 표시. |
| 프로토콜-10 | ④ | UDP Length = **헤더(8바이트) + 데이터**의 전체 길이(바이트 단위, 최소값 8). IP 헤더는 포함하지 않는다. |
| 프로토콜-11 | ② | **MSS**(Maximum Segment Size) = TCP 데이터 부분의 최대 크기(이더넷에서 보통 1500 − IP 20 − TCP 20 = 1460바이트). MTU는 링크 계층이 한 번에 실을 수 있는 IP 패킷 최대 크기, RTT는 왕복 시간, TTL은 패킷 수명. |
| 프로토콜-12 | ① | **Slow Start**는 이름과 달리 RTT마다 cwnd가 **지수적(2배)**으로 증가. 혼잡 회피는 선형 증가, 빠른 재전송은 중복 ACK 3개 시 즉시 재전송, Stop-and-Wait는 혼잡 제어 단계가 아닌 단순 ARQ 방식. |
| 프로토콜-13 | ④ | **arp -a** = ARP 캐시(IP↔MAC) 조회 (`arp -d` 삭제, `arp -s` 정적 등록). netstat -r과 route print는 라우팅 테이블, ipconfig /all은 자신의 IP·MAC·DNS 등 상세 설정. |
| 프로토콜-14 | ③ | Well-known 포트는 **0~1023**. 1024~49151은 등록(Registered) 포트, 49152~65535는 동적 포트. |
| 프로토콜-15 | ① | POP3는 **110**번. **143은 IMAP**. SSH 22, SMTP 25, HTTPS 443은 옳다. |
| 프로토콜-16 | ② | 많은 레코드를 한꺼번에 신뢰성 있게 넘겨야 하는 **영역 전송(AXFR/IXFR)** 은 TCP 53을 쓴다(응답이 너무 큰 경우도 TCP로 재시도). 역방향 조회도 일반 질의이므로 UDP. |
| 프로토콜-17 | ① | **Stratum 0** = 기준 시계 장치, Stratum 1 = 그 장치에 직접 연결된 시간 서버, 숫자가 커질수록 기준에서 멀어진다(15까지 유효, 16은 동기화되지 않음). NTP는 UDP 123. |
| 프로토콜-18 | ③ | 1xx 정보, 2xx **성공**, 3xx **리다이렉션**, 4xx **클라이언트 오류**(400·403·404), 5xx **서버 오류**(500·503). |
| 프로토콜-19 | ① | **MX(Mail eXchanger)** 레코드가 메일 서버 지정. CNAME은 별칭, A는 이름→IPv4, PTR은 IP→이름(역방향). |
| 프로토콜-20 | ④ | DHCP는 **DORA: Discover → Offer → Request → Ack**. |
| 프로토콜-21 | ③ | **SetRequest** = 값 변경(설정). GetRequest는 값 조회, GetNextRequest는 MIB 트리의 다음 객체 조회, Trap은 에이전트가 이벤트 발생 시 매니저에게 먼저 알리는 메시지. |
| 프로토콜-22 | ④ | 다익스트라 알고리즘은 **OSPF 등 링크 상태** 방식. RIP은 **벨만-포드** 알고리즘을 사용하는 거리 벡터 방식. ①②③은 RIP의 올바른 특징. |
| 프로토콜-23 | ② | **IS-IS** = OSI 계열 링크 상태 IGP(다익스트라 SPF). EIGRP는 시스코 하이브리드, RIP은 거리 벡터, EGP는 초기 AS 간 프로토콜(현재는 BGP가 대체). |
| 프로토콜-24 | ④ | AD는 **작을수록 우선**: 정적 1 < EIGRP 90 < OSPF 110 < RIP 120. 따라서 **정적 경로**가 라우팅 테이블에 등록된다. |
| 프로토콜-25 | ① | **Split Horizon**: 학습한 인터페이스로 같은 경로를 되돌려 광고하지 않음. Hold-down은 일정 시간 갱신 무시, Route Poisoning은 끊긴 경로를 무한대(16)로 광고, Triggered Update는 변화 즉시 업데이트. |

**정답 분포:** ① 6개 / ② 6개 / ③ 6개 / ④ 7개
