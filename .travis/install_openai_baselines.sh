OPENAI_BASELINES=$TRAVIS_BUILD_DIR/openai_baselines

if [ ! "$(ls $OPENAI_BASELINES)" ]; then
    mkdir -p $OPENAI_BASELINES

    cd $OPENAI_BASELINES

    wget -O baselines.zip https://github.com/openai/baselines/archive/master.zip

    sudo apt-get install -y unzip

    unzip baselines.zip -d .
fi  

cd $OPENAI_BASELINES/baselines-master

foldable pip install -e .
