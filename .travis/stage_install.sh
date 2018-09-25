
for script in \
    install_orange.sh \
    install_pyqt.sh
do
    foldable source $TRAVIS_BUILD_DIR/.travis/$script
done
