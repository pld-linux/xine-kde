# TODO:		Add pl to desktop file.
Summary:	KDE xine DVD integration
Summary(pl):	Integracja xine DVD z KDE
Name:		xine-kde
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
# Source0:	http://kde-apps.org/content/download.php?content=34926&id=1
Source0:	http://kde-apps.org/content/files/34926-kde_media_video_dvd-%{version}.tar.bz2
# Source0-md5:	b1ede2013bc0a161d698ed27cf8fbc4c
URL:		http://kde-apps.org/content/show.php?content=34926
Requires:	kdebase-desktop
Requires:	xine-input-dvd
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A little servicetype which lets to video dvds automatically in Xine.
Includes a script to translate a media:/ URL into a device using dcop.

%description -l pl
Ma³y dodatek servicetype, który pozwala na automatyczne odtwarzanie
w³o¿onej do czytnika p³yty DVD w programie Xine. Zawiera skrypt
t³umacz±cy URL media:/ na urz±dzenie przy pomocy dcop.

%prep
%setup -q -n kde_media_video_dvd-%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install kde_media_url_to_device.sh $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus
install Play_Video_DVD_in_Xine.desktop $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kde_media_url_to_device.sh
%{_datadir}/apps/konqueror/servicemenus/Play_Video_DVD_in_Xine.desktop
