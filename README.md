# ArcMap-LULC-Keyshortcuts

An advanced custom modification for ArcMap 10.x, specifically designed to speed up the **digitisation of land cover (Land Cover / LULC)** workflow.

When mapping land cover, the most effective method is wall-to-wall mapping (creating a single giant polygon covering the full extent of the image, then splitting it up (Cut) and occasionally merging it (Merge) until the entire area has been classified without any gaps). This project eliminates the tedious mouse click delays by adapting **OSM iD Editor-style muscle memory (finger habits)** into the old ArcMap workflow.

This project combines ArcMap’s built-in features, a clever Python add-in, and AutoHotkey (AHK) to push beyond the limitations of the software’s built-in *shortcuts*.


## Repository Structure

```text
ArcMap-LULC-Keyshortcuts/
│
├── AHK_Script/
│   ├── ArcMap_iD_Editor.ahk         # Raw AutoHotkey script (v2)
│   └── ArcMap_iD_Editor.exe         # Compiled script (Standalone/Ready to use)
│
├── LULC_Tool_Addin/                       # Source code Python Add-In
│   ├── Install/                     
│   │   └── LULC_Tool_addin.py       # Python core logic for toggling smart layers
│   ├── makeaddin.py                 # Esri’s built-in script compiler
│   ├── config.xml                   # Add-In metadata configuration file
│   └── LULC_Tool.esriaddin          # Ready-to-use Add-In Installer
│
├── .gitignore                       # Ignore file cache/system
├── LICENSE                          # MIT Licence
└── README.md                        # DDocumentation for this project
```

**IMPORTANT WARNING (AUTOHOTKEY):**

This AutoHotkey (AHK) script modifies the functions of the main keyboard keys (for example, `Space` bar becomes a left-click). It is essential to temporarily suspend the AHK script running in the background when typing text (for example, when filling in the Attribute Table) or when switching to an application other than ArcMap.

To suspend: Right-click the green ‘H’ icon in the System Tray (bottom right corner of the Windows taskbar) -> select ‘Suspend Hotkeys’. Failure to do so may result in typing errors or unintended automatic clicks.

## Main Feature
Although it uses a button layout similar to that for creating buildings/roads in the iD Editor (1, 2, 3, W), its functions have been completely repurposed to streamline the Cut & Merge LULC workflow. Your fingers do not need to move from the left-hand home row (W-A-S-D).

### 1. Main Navigation & Operation 
| ArcMap Actions | Shortcut | Technical Implementation | Documentation |
|---|:---:|---|:---:|
| Adding a Point (Vertex) | `Space` | Pressing the `Space` key while sketching or splitting is simulated as a left mouse click | `GIF` | 
| Select Features | `1` | Immediately select the Selection Tool to select a polygon | `GIF` |
| Cut / Split Polygons | `2` | Call the Cut Polygons Tool directly | `GIF` |
| Clear Selection | `3` | Deleting the selected polygons  | `GIF` |

### 2. Merge Management (Merge Polygons)
| ArcMap Actions | Shortcut | Technical Implementation | Documentation |
|---|:---:|---|:---:|
| Open the Merge Window | `Ctrl + Q` | Open the Merge dialogue box instantly | `GIF` | 
| Select Merge Feature (Down) | `Ctrl + Q` | Go straight to the next feature in the list | `GIF` |
| Select Merge Feature (Up) | `Shift + Q` | Go straight to the feature above it in the list | `GIF` |

**Technical Notes on Merging:**

Due to inherent limitations in ArcObjects, navigating through the list using the keyboard will not trigger the ‘Flash’ effect (green flash) on the polygons on screen. If you need to see the reference polygons flash, it is still recommended that you click on the list using the mouse.

### 3. Utility
| ArcMap Actions | Shortcut | Technical Implementation | Documentation |
|---|:---:|---|:---:|
| Smart Toggle Layer (On/Off) | `W` | Toggle the visibility of the currently selected (highlighted) layer in the Table of Contents (TOC). | `GIF` | 
| Save Edits | `Shift + S` | Save the editing session | `GIF` |

## System Requirement
- **ArcMap 10.x** (Tested on version 10.8)
- **AutoHotkey v2.0** (Optional – only if you wish to modify the `.ahk` script. If you are simply a user, just run the `.exe` version)

## Instalation Guide
The installation is divided into three stages. Follow the steps below in order.

### Stage 1: Configuring ArcMap’s Default Shortcuts
As ArcMap blocks single-key shortcuts (single keys such as letters without modifiers), the foundation is set up first using the Ctrl key (AHK will simplify this later):
1. Open ArcMap, go to the menu `Customise` > `Customise Mode...` > `Commands` tab > click `Keyboard...` in the bottom corner.
2. Set up the following shortcuts:
    - Editor Category -> `Edit Tool` -> Assign to `Ctrl + 1`
    - Editor Category -> `Cut Polygons` -> Assign to `Ctrl + 2`
    - Selection Category -> `Clear Selected Features` -> Assign to `Ctrl + 3`
    - Editor Category -> `Merge...` -> Assign to `Ctrl + Q`
    - Editor Category -> `Save Edits` -> Assign to `Ctrl + Shift + S`
3. Click Close

### Stage 2: Installing the Python Add-In (Smart Toggle Layer)
1. Open the `LULC_Tool_Addin` folder from this repository.
2. Double-click the `LULC_Tool.esriaddin` file. Click ‘Install Add-In’.
3. Open (or restart) ArcMap, then go to `Customise` > `Customise Mode...` > `Commands` tab > `Keyboard...`
4. Find and click on the category tab called `LULC_Tool` on the left.
5. Find the `Toggle Top Layer` command on the right, then assign the shortcut `Ctrl + W` to it
6. Click Close

### Stage 3: Running AutoHotkey (AHK)
This is the macro that will trick ArcMap into recognising single keys (Space, 1, 2, 3, W).

1. Open the folder `AHK_Script`.
2. **Standard Users:** Run the `ArcMap_iD_Editor.exe` file. (The program runs in the background, indicated by a green ‘H’ icon in the System Tray at the bottom right of the Windows taskbar).
3. **Developers:** Modify and run directly from the raw `ArcMap_iD_Editor.ahk` file (requires AutoHotkey v2).

*Designed to protect the finger joints of land-cover digitisers. Contributions and pull requests are very welcome!*