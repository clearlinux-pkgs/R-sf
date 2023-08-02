#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-sf
Version  : 1.0.14
Release  : 82
URL      : https://cran.r-project.org/src/contrib/sf_1.0-14.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sf_1.0-14.tar.gz
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
encode spatial vector data. Binds to 'GDAL' for reading and writing
    data, to 'GEOS' for geometrical operations, and to 'PROJ' for
    projection conversions and datum transformations. Uses by default the 's2'
    package for spherical geometry operations on ellipsoidal (long/lat) coordinates.

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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689092262

%install
export SOURCE_DATE_EPOCH=1689092262
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/sf/doc/sf7.R
/usr/lib64/R/library/sf/doc/sf7.Rmd
/usr/lib64/R/library/sf/doc/sf7.html
/usr/lib64/R/library/sf/docker/alma/Dockerfile
/usr/lib64/R/library/sf/docker/alma/build_command
/usr/lib64/R/library/sf/docker/alma/vito.repo
/usr/lib64/R/library/sf/docker/arrow/Dockerfile
/usr/lib64/R/library/sf/docker/base/Dockerfile
/usr/lib64/R/library/sf/docker/bionic/Dockerfile
/usr/lib64/R/library/sf/docker/centos/Dockerfile
/usr/lib64/R/library/sf/docker/cran/Dockerfile
/usr/lib64/R/library/sf/docker/custom/Dockerfile
/usr/lib64/R/library/sf/docker/devel/Dockerfile
/usr/lib64/R/library/sf/docker/fedora/Dockerfile
/usr/lib64/R/library/sf/docker/gdal/Dockerfile
/usr/lib64/R/library/sf/docker/gdal304/Dockerfile
/usr/lib64/R/library/sf/docker/geos/Dockerfile
/usr/lib64/R/library/sf/docker/lowest/Dockerfile
/usr/lib64/R/library/sf/docker/postgis/Dockerfile
/usr/lib64/R/library/sf/docker/spcosa/Dockerfile
/usr/lib64/R/library/sf/docker/static/Dockerfile
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
/usr/lib64/R/library/sf/include/sf.h
/usr/lib64/R/library/sf/include/sf_RcppExports.h
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
/usr/lib64/R/library/sf/tests/testthat/s2.R
/usr/lib64/R/library/sf/tests/testthat/test-grid.R
/usr/lib64/R/library/sf/tests/testthat/test-normalize.R
/usr/lib64/R/library/sf/tests/testthat/test-shift_longitude.R
/usr/lib64/R/library/sf/tests/testthat/test_bbox.R
/usr/lib64/R/library/sf/tests/testthat/test_collection_extract.R
/usr/lib64/R/library/sf/tests/testthat/test_crs.R
/usr/lib64/R/library/sf/tests/testthat/test_gdal.R
/usr/lib64/R/library/sf/tests/testthat/test_geos.R
/usr/lib64/R/library/sf/tests/testthat/test_plot.R
/usr/lib64/R/library/sf/tests/testthat/test_postgis_ODBC.R
/usr/lib64/R/library/sf/tests/testthat/test_postgis_RPostgreSQL.R
/usr/lib64/R/library/sf/tests/testthat/test_postgis_RPostgres.R
/usr/lib64/R/library/sf/tests/testthat/test_project.R
/usr/lib64/R/library/sf/tests/testthat/test_read.R
/usr/lib64/R/library/sf/tests/testthat/test_sample.R
/usr/lib64/R/library/sf/tests/testthat/test_sf.R
/usr/lib64/R/library/sf/tests/testthat/test_sfc.R
/usr/lib64/R/library/sf/tests/testthat/test_sfg.R
/usr/lib64/R/library/sf/tests/testthat/test_sp.R
/usr/lib64/R/library/sf/tests/testthat/test_st_cast.R
/usr/lib64/R/library/sf/tests/testthat/test_tidy.R
/usr/lib64/R/library/sf/tests/testthat/test_tm.R
/usr/lib64/R/library/sf/tests/testthat/test_valid.R
/usr/lib64/R/library/sf/tests/testthat/test_vctrs.R
/usr/lib64/R/library/sf/tests/testthat/test_wkb.R
/usr/lib64/R/library/sf/tests/testthat/test_wkt.R
/usr/lib64/R/library/sf/tests/testthat/test_write.R
/usr/lib64/R/library/sf/tests/testthat/test_zm_range.R
/usr/lib64/R/library/sf/tests/units.R
/usr/lib64/R/library/sf/tests/units.Rout.save
/usr/lib64/R/library/sf/tests/wkb.R
/usr/lib64/R/library/sf/tests/wkb.Rout.save
/usr/lib64/R/library/sf/tif/geomatrix.tif

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sf/libs/sf.so
/usr/lib64/R/library/sf/libs/sf.so.avx2
/usr/lib64/R/library/sf/libs/sf.so.avx512
