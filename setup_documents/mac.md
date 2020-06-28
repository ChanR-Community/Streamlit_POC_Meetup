# Setting Up Streamlit Environment on Mac

## Step 1: Install Homebrew

- Click on the Magnifying Glass on Top Right

- Type in Terminal within the Spotlight Window

- Hit Enter

- Within the prompt, copy and paste the following:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

## Step 2: Install Git, Atom

- Within the prompt, type in the following:

```
brew install git && brew cask install atom
```

## Step 3: Set Up Miniconda
- Get the bash script for [Miniconda](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh)
- Within your Terminal, type in the following:
```
sh ~/Downloads/*.sh
```
- Hold enter until the installer prompt reaches the very bottom.
- Type in ``yes`` and hit enter.
- Hit enter when asked location.

## Step 4: Create a Virtual Environment
- Type in the following:
```
conda create -n chanr_community python=3.6.9 anaconda
```
- When the prompt opens, type in ``y`` and hit enter.

- Once all packages finish installing, type in the following:
```
conda activate chanr_community
```

- Then within the prompt, install streamlit and wordcloud
```
pip install streamlit wordcloud
```

## Step 6: Set Up Hydrogen

- Within the prompt, type the following:
```
cd Desktop && mkdir streamlit_workshop && cd streamlit_workshop && atom .
```
- When the Atom window opens, close the Welcome Guide.
- Uncheck the box that says Show Welcome Guide on Startup.
- Close the tab.
- Support Atom by allowing telemetry consent.
- Hold ctrl and press ,
- Within the pane, select Install.
- Install Hydrogen on right window.

## Step 7: Register Your Virtual Environment as an Acceptable Kernel on Hydrogen

- Within the prompt, type in the following:
```
python -m ipykernel install --user --name=chanr_community
```

- Restart Atom by Closing the tab and typing the following in the prompt:
```
atom .
```
