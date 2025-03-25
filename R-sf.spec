#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-sf
Version  : 1.0.20
Release  : 132
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/sf_1.0-20.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/sf_1.0-20.tar.gz
Summary  : Simple Features for R
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: R-sf-lib = %{version}-%{release}
Requires: R-DBI
Requires: R-Rcpp
Requires: R-classInt
Requires: R-magrittr
Requires: R-s2
Requires: R-units
BuildRequires : R-DBI
BuildRequires : R-Rcpp
BuildRequires : R-classInt
BuildRequires : R-magrittr
BuildRequires : R-s2
BuildRequires : R-units
BuildRequires : buildreq-R
BuildRequires : gdal-dev
BuildRequires : geos-dev
BuildRequires : pkgconfig(sqlite3)
BuildRequires : proj-dev

%description
encode and analyze spatial vector data. Binds to 'GDAL'

%package dev
Summary: dev components for the R-sf package.
Group: Development
Requires: R-sf-lib = %{version}-%{release}
Provides: R-sf-devel = %{version}-%{release}
Requires: R-sf = %{version}-%{release}

%description dev
dev components for the R-sf package.


%package lib
Summary: lib components for the R-sf package.
Group: Libraries

%description lib
lib components for the R-sf package.


%prep
%setup -q -n sf
pushd ..
cp -a sf buildavx2
popd
pushd ..
cp -a sf buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742913707

%install
export SOURCE_DATE_EPOCH=1742913707
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/sf/demo/ggplot.R
/usr/lib64/R/library/sf/demo/meuse_sf.R
/usr/lib64/R/library/sf/demo/nc.R
/usr/lib64/R/library/sf/demo/twitter.R
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
/usr/lib64/R/library/sf/doc/sf7.R
/usr/lib64/R/library/sf/doc/sf7.Rmd
/usr/lib64/R/library/sf/doc/sf7.html
/usr/lib64/R/library/sf/docker/alma/Dockerfile
/usr/lib64/R/library/sf/docker/alma/build_command
/usr/lib64/R/library/sf/docker/alma/vito.repo
/usr/lib64/R/library/sf/docker/arrow/Dockerfile
/usr/lib64/R/library/sf/docker/base/Dockerfile
/usr/lib64/R/library/sf/docker/bionic/Dockerfile
/usr/lib64/R/library/sf/docker/cran/Dockerfile
/usr/lib64/R/library/sf/docker/custom/Dockerfile
/usr/lib64/R/library/sf/docker/devel/Dockerfile
/usr/lib64/R/library/sf/docker/fedora/Dockerfile
/usr/lib64/R/library/sf/docker/gdal/Dockerfile
/usr/lib64/R/library/sf/docker/gdal304/Dockerfile
/usr/lib64/R/library/sf/docker/gdalGH/Dockerfile
/usr/lib64/R/library/sf/docker/geos/Dockerfile
/usr/lib64/R/library/sf/docker/lowest/Dockerfile
/usr/lib64/R/library/sf/docker/parquet/Dockerfile
/usr/lib64/R/library/sf/gml/20170930_OB_530964_UKSH.xml.gz
/usr/lib64/R/library/sf/gml/fmi_test.gml
/usr/lib64/R/library/sf/gpkg/b_pump.gpkg
/usr/lib64/R/library/sf/gpkg/buildings.gpkg
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
/usr/lib64/R/library/sf/tests/aggregate.R
/usr/lib64/R/library/sf/tests/aggregate.Rout.save
/usr/lib64/R/library/sf/tests/bgmap.rda
/usr/lib64/R/library/sf/tests/cast.R
/usr/lib64/R/library/sf/tests/cast.Rout.save
/usr/lib64/R/library/sf/tests/crs.R
/usr/lib64/R/library/sf/tests/crs.Rout.save
/usr/lib64/R/library/sf/tests/dist.R
/usr/lib64/R/library/sf/tests/dist.Rout.save
/usr/lib64/R/library/sf/tests/dplyr.R
/usr/lib64/R/library/sf/tests/dplyr.Rout.save
/usr/lib64/R/library/sf/tests/empty.R
/usr/lib64/R/library/sf/tests/empty.Rout.save
/usr/lib64/R/library/sf/tests/full.R
/usr/lib64/R/library/sf/tests/full.Rout.save
/usr/lib64/R/library/sf/tests/gdal_geom.R
/usr/lib64/R/library/sf/tests/gdal_geom.Rout.save
/usr/lib64/R/library/sf/tests/geos.R
/usr/lib64/R/library/sf/tests/geos.Rout.save
/usr/lib64/R/library/sf/tests/graticule.R
/usr/lib64/R/library/sf/tests/graticule.Rout.save
/usr/lib64/R/library/sf/tests/grid.R
/usr/lib64/R/library/sf/tests/grid.Rout.save
/usr/lib64/R/library/sf/tests/maps.R
/usr/lib64/R/library/sf/tests/maps.Rout.save
/usr/lib64/R/library/sf/tests/plot.R
/usr/lib64/R/library/sf/tests/plot.Rout.save
/usr/lib64/R/library/sf/tests/read.R
/usr/lib64/R/library/sf/tests/read.Rout.save
/usr/lib64/R/library/sf/tests/roundtrip.R
/usr/lib64/R/library/sf/tests/roundtrip.Rout.save
/usr/lib64/R/library/sf/tests/s2.R
/usr/lib64/R/library/sf/tests/s2.Rout.save
/usr/lib64/R/library/sf/tests/sample.R
/usr/lib64/R/library/sf/tests/sample.Rout.save
/usr/lib64/R/library/sf/tests/sfc.R
/usr/lib64/R/library/sf/tests/sfc.Rout.save
/usr/lib64/R/library/sf/tests/sfg.R
/usr/lib64/R/library/sf/tests/sfg.Rout.save
/usr/lib64/R/library/sf/tests/spatstat.R
/usr/lib64/R/library/sf/tests/spatstat.Rout.save
/usr/lib64/R/library/sf/tests/stars.R
/usr/lib64/R/library/sf/tests/stars.Rout.save
/usr/lib64/R/library/sf/tests/testthat.R
/usr/lib64/R/library/sf/tests/testthat/Rplots.pdf
/usr/lib64/R/library/sf/tests/testthat/test-bbox.R
/usr/lib64/R/library/sf/tests/testthat/test-collection_extract.R
/usr/lib64/R/library/sf/tests/testthat/test-crs.R
/usr/lib64/R/library/sf/tests/testthat/test-gdal.R
/usr/lib64/R/library/sf/tests/testthat/test-geos.R
/usr/lib64/R/library/sf/tests/testthat/test-grid.R
/usr/lib64/R/library/sf/tests/testthat/test-normalize.R
/usr/lib64/R/library/sf/tests/testthat/test-plot.R
/usr/lib64/R/library/sf/tests/testthat/test-postgis_ODBC.R
/usr/lib64/R/library/sf/tests/testthat/test-postgis_RPostgreSQL.R
/usr/lib64/R/library/sf/tests/testthat/test-postgis_RPostgres.R
/usr/lib64/R/library/sf/tests/testthat/test-proj.R
/usr/lib64/R/library/sf/tests/testthat/test-read.R
/usr/lib64/R/library/sf/tests/testthat/test-s2.R
/usr/lib64/R/library/sf/tests/testthat/test-sample.R
/usr/lib64/R/library/sf/tests/testthat/test-sf.R
/usr/lib64/R/library/sf/tests/testthat/test-sfc.R
/usr/lib64/R/library/sf/tests/testthat/test-sfg.R
/usr/lib64/R/library/sf/tests/testthat/test-shift_longitude.R
/usr/lib64/R/library/sf/tests/testthat/test-sp.R
/usr/lib64/R/library/sf/tests/testthat/test-st_cast.R
/usr/lib64/R/library/sf/tests/testthat/test-tidyverse-vctrs.R
/usr/lib64/R/library/sf/tests/testthat/test-tidyverse.R
/usr/lib64/R/library/sf/tests/testthat/test-tm.R
/usr/lib64/R/library/sf/tests/testthat/test-valid.R
/usr/lib64/R/library/sf/tests/testthat/test-wkb.R
/usr/lib64/R/library/sf/tests/testthat/test-wkt.R
/usr/lib64/R/library/sf/tests/testthat/test-write.R
/usr/lib64/R/library/sf/tests/testthat/test-zm_range.R
/usr/lib64/R/library/sf/tests/units.R
/usr/lib64/R/library/sf/tests/units.Rout.save
/usr/lib64/R/library/sf/tests/wkb.R
/usr/lib64/R/library/sf/tests/wkb.Rout.save
/usr/lib64/R/library/sf/tif/geomatrix.tif

%files dev
%defattr(-,root,root,-)
/usr/lib64/R/library/sf/include/sf.h
/usr/lib64/R/library/sf/include/sf_RcppExports.h

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/sf/libs/sf.so
/V4/usr/lib64/R/library/sf/libs/sf.so
/usr/lib64/R/library/sf/libs/sf.so
