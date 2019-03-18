#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sf
Version  : 0.7.3
Release  : 5
URL      : https://cran.r-project.org/src/contrib/sf_0.7-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sf_0.7-3.tar.gz
Summary  : Simple Features for R
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: R-sf-lib = %{version}-%{release}
Requires: R-DBI
Requires: R-Rcpp
Requires: R-classInt
Requires: R-dplyr
Requires: R-rgeos
Requires: R-sp
Requires: R-units
BuildRequires : R-DBI
BuildRequires : R-Rcpp
BuildRequires : R-classInt
BuildRequires : R-dplyr
BuildRequires : R-rgeos
BuildRequires : R-sp
BuildRequires : R-units
BuildRequires : buildreq-R
BuildRequires : gdal-dev
BuildRequires : geos-dev
BuildRequires : proj-dev

%description
encode spatial vector data. Binds to 'GDAL' for reading and writing
    data, to 'GEOS' for geometrical operations, and to 'PROJ' for
    projection conversions and datum transformations.

%package lib
Summary: lib components for the R-sf package.
Group: Libraries

%description lib
lib components for the R-sf package.


%prep
%setup -q -c -n sf

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551647263

%install
export SOURCE_DATE_EPOCH=1551647263
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sf
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sf
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sf
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library sf|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sf/CITATION
/usr/lib64/R/library/sf/DESCRIPTION
/usr/lib64/R/library/sf/INDEX
/usr/lib64/R/library/sf/LICENSE
/usr/lib64/R/library/sf/Meta/Rd.rds
/usr/lib64/R/library/sf/Meta/demo.rds
/usr/lib64/R/library/sf/Meta/features.rds
/usr/lib64/R/library/sf/Meta/hsearch.rds
/usr/lib64/R/library/sf/Meta/links.rds
/usr/lib64/R/library/sf/Meta/nsInfo.rds
/usr/lib64/R/library/sf/Meta/package.rds
/usr/lib64/R/library/sf/Meta/vignette.rds
/usr/lib64/R/library/sf/NAMESPACE
/usr/lib64/R/library/sf/NEWS.md
/usr/lib64/R/library/sf/R/sf
/usr/lib64/R/library/sf/R/sf.rdb
/usr/lib64/R/library/sf/R/sf.rdx
/usr/lib64/R/library/sf/csv/pt.csv
/usr/lib64/R/library/sf/demo/affine.R
/usr/lib64/R/library/sf/demo/basic.R
/usr/lib64/R/library/sf/demo/bm_wkb.R
/usr/lib64/R/library/sf/demo/ggplot.R
/usr/lib64/R/library/sf/demo/meuse_sf.R
/usr/lib64/R/library/sf/demo/nc.R
/usr/lib64/R/library/sf/demo/twitter.R
/usr/lib64/R/library/sf/demo/webmap.R
/usr/lib64/R/library/sf/doc/index.html
/usr/lib64/R/library/sf/doc/sf1.R
/usr/lib64/R/library/sf/doc/sf1.Rmd
/usr/lib64/R/library/sf/doc/sf1.html
/usr/lib64/R/library/sf/doc/sf2.R
/usr/lib64/R/library/sf/doc/sf2.Rmd
/usr/lib64/R/library/sf/doc/sf2.html
/usr/lib64/R/library/sf/doc/sf3.R
/usr/lib64/R/library/sf/doc/sf3.Rmd
/usr/lib64/R/library/sf/doc/sf3.html
/usr/lib64/R/library/sf/doc/sf4.R
/usr/lib64/R/library/sf/doc/sf4.Rmd
/usr/lib64/R/library/sf/doc/sf4.html
/usr/lib64/R/library/sf/doc/sf5.R
/usr/lib64/R/library/sf/doc/sf5.Rmd
/usr/lib64/R/library/sf/doc/sf5.html
/usr/lib64/R/library/sf/doc/sf6.R
/usr/lib64/R/library/sf/doc/sf6.Rmd
/usr/lib64/R/library/sf/doc/sf6.html
/usr/lib64/R/library/sf/docker/base/Dockerfile
/usr/lib64/R/library/sf/docker/cran/Dockerfile
/usr/lib64/R/library/sf/docker/custom/Dockerfile
/usr/lib64/R/library/sf/docker/devel/Dockerfile
/usr/lib64/R/library/sf/docker/fedora/Dockerfile
/usr/lib64/R/library/sf/docker/gdal/Dockerfile
/usr/lib64/R/library/sf/docker/lowest/Dockerfile
/usr/lib64/R/library/sf/gml/20170930_OB_530964_UKSH.xml.gz
/usr/lib64/R/library/sf/gml/fmi_test.gml
/usr/lib64/R/library/sf/gpkg/nc.gpkg
/usr/lib64/R/library/sf/gpkg/nospatial.gpkg
/usr/lib64/R/library/sf/gpkg/tl.gpkg
/usr/lib64/R/library/sf/help/AnIndex
/usr/lib64/R/library/sf/help/aliases.rds
/usr/lib64/R/library/sf/help/figures/logo.png
/usr/lib64/R/library/sf/help/paths.rds
/usr/lib64/R/library/sf/help/sf.rdb
/usr/lib64/R/library/sf/help/sf.rdx
/usr/lib64/R/library/sf/html/00Index.html
/usr/lib64/R/library/sf/html/R.css
/usr/lib64/R/library/sf/include/sf.h
/usr/lib64/R/library/sf/include/sf_RcppExports.h
/usr/lib64/R/library/sf/libs/symbols.rds
/usr/lib64/R/library/sf/nc/cropped.nc
/usr/lib64/R/library/sf/osm/overpass.osm
/usr/lib64/R/library/sf/shape/nc.dbf
/usr/lib64/R/library/sf/shape/nc.prj
/usr/lib64/R/library/sf/shape/nc.shp
/usr/lib64/R/library/sf/shape/nc.shx
/usr/lib64/R/library/sf/shape/olinda1.dbf
/usr/lib64/R/library/sf/shape/olinda1.prj
/usr/lib64/R/library/sf/shape/olinda1.shp
/usr/lib64/R/library/sf/shape/olinda1.shx
/usr/lib64/R/library/sf/shape/storms_xyz.dbf
/usr/lib64/R/library/sf/shape/storms_xyz.shp
/usr/lib64/R/library/sf/shape/storms_xyz.shx
/usr/lib64/R/library/sf/shape/storms_xyz_feature.dbf
/usr/lib64/R/library/sf/shape/storms_xyz_feature.shp
/usr/lib64/R/library/sf/shape/storms_xyz_feature.shx
/usr/lib64/R/library/sf/shape/storms_xyzm.dbf
/usr/lib64/R/library/sf/shape/storms_xyzm.shp
/usr/lib64/R/library/sf/shape/storms_xyzm.shx
/usr/lib64/R/library/sf/shape/storms_xyzm_feature.dbf
/usr/lib64/R/library/sf/shape/storms_xyzm_feature.shp
/usr/lib64/R/library/sf/shape/storms_xyzm_feature.shx
/usr/lib64/R/library/sf/sqlite/b.sqlite
/usr/lib64/R/library/sf/sqlite/meuse.sqlite
/usr/lib64/R/library/sf/sqlite/nc.sqlite
/usr/lib64/R/library/sf/sqlite/test3.sqlite
/usr/lib64/R/library/sf/tif/geomatrix.tif

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sf/libs/sf.so
/usr/lib64/R/library/sf/libs/sf.so.avx2
/usr/lib64/R/library/sf/libs/sf.so.avx512
