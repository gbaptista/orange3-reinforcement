foldable pip install -U pip

foldable sudo apt-get install -y libopenmpi-dev
foldable sudo apt-get install -y python-mpi4py

cat requirements-dev.txt \
    requirements.txt |
    while read dep; do
        dep="${dep%%#*}"  # Strip the comment
        [ "$dep" ] &&
            foldable pip install $dep
    done

cd $TRAVIS_BUILD_DIR
