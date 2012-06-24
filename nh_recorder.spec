Summary:	script(1) on sterides
Summary(pl.UTF-8):   script(1) na sterydach
Name:		nh_recorder
Version:	1.0
Release:	2
License:	GPL
Group:		Applications
Source0:	http://www.itp.uni-hannover.de/~dennha/nh_recorder/%{name}-%{version}.sources.tar.gz
# Source0-md5:	ecf7b10eadc2dd53385137bb44979c38
URL:		http://nh-recorder.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Nethack-Recorder ("nh_recorder") allows you to record your entire
Nethack game (or any other text mode activity) into a movie file.

The Nethack-Player ("nh_player") allows you to replay your movie files
at different speed or starting from a certain time index. With these
two programs you can review your favourite Nethack-games. Watch and
enjoy!

%description -l pl.UTF-8
Nethackowy nagrywacz ("nh_recorder") pozwala zapisać cały przebieg gry
w Nethacka (lub dowolne inne działania w trybie tekstowym) do pliku.

Nethackowy odtwarzacz ("nh_player") odtwarza te pliki z różnymi
prędkościami, lub/i zaczynając od zadanego miejsca. Wykorzystując te
dwa narzędzia możesz ponownie obejrzeć swoje ulubione sesje Nethacka.

%prep
%setup -q

%build
%{__make} CC="%{__cc}" \
	CCFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install nh_{player,recorder} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
