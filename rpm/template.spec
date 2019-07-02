Name:           ros-melodic-microstrain-3dmgx2-imu
Version:        1.5.13
Release:        1%{?dist}
Summary:        ROS microstrain_3dmgx2_imu package

Group:          Development/Libraries
License:        LGPL
URL:            http://www.ros.org/wiki/microstrain_3dmgx2_imu
Source0:        %{name}-%{version}.tar.gz

Requires:       log4cxx-devel
Requires:       ros-melodic-diagnostic-updater
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-self-test
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
Requires:       ros-melodic-tf
BuildRequires:  log4cxx-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-diagnostic-updater
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-self-test
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs
BuildRequires:  ros-melodic-tf

%description
A driver for IMUs compatible the microstrain 3DM-GX2 and 3DM-GX3 protocol.
Includes a heavily modified standalone driver pulled from the player
distribution, and a ROS node.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Jul 02 2019 Chad Rockey <chadrockey@gmail.com> - 1.5.13-1
- Autogenerated by Bloom

* Fri May 03 2019 Chad Rockey <chadrockey@gmail.com> - 1.5.12-1
- Autogenerated by Bloom

* Sat Mar 30 2019 Chad Rockey <chadrockey@gmail.com> - 1.5.12-0
- Autogenerated by Bloom

