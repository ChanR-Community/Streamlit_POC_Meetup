# Setting Up Streamlit Environment on Windows

## Step 1: Install Chocolatey

- Open an Administrator Command Prompt

- Within the prompt, copy and paste the following:

```
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command " [System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

## Step 2: Install Git, Atom

- Within the prompt, type in the following:

```
refreshenv
choco install git atom
```

## Step 3: Set Up Atom CLI Tools

- Within the prompt, type in the following:
```
refreshenv
cd %localappdata%
```
- Type in ``cd atom/atom`` then press tab to autocomplete

- Finally, type in ``atom.exe --squirrel-install``

## Step 4: Set Up Miniconda
- Get the official [Miniconda executable](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)
- Go through the installation process
- Ensure that the ``ADD to PATH`` checkbox is selected.

## Step 5: Create a Virtual Environment
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
cd ../../Users/${Your Computer Username}/Desktop
mkdir streamlit_workshop && cd streamlit_workshop
mkdir apps && atom .
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
