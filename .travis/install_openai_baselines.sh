OPENAI_BASELINES=$TRAVIS_BUILD_DIR/openai_baselines

if [ ! "$(ls $if [ ! "$(ls $OPENAI_BASELINES)" ]; then)" ]; then
    mkdir -p $OPENAI_BASELINES

    cd $OPENAI_BASELINES

    wget -O baselines.zip https://github.com/openai/baselines/archive/master.zip

    unzip baselines.zip -d .
fi  

cd $OPENAI_BASELINES/baselines-master

foldable pip install -e .