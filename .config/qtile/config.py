from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"

applications = {
    'terminal': 'kitty',
    'browser': 'brave-browser-nightly --password-store=basic',
    'private_browser': 'brave-browser-nightly --incognito',
    'tor_browser': 'brave-browser-nightly --incognito --tor',
    'obs': 'obs',
    'docker': 'systemctl start --user docker-desktop',
    'docker_restart': 'systemctl restart --user docker-desktop',
    'explorer': 'kitty ranger',
    'media': 'vlc',
    'database_client': 'dbeaver',
    'screen_shot': 'flameshot gui',
}

keys = [
    Key( [ mod ], 'h', lazy.layout.left(), desc='Move focus to left' ),
    Key( [ mod ], 'l', lazy.layout.right(), desc='Move focus to right' ),
    Key( [ mod ], 'j', lazy.layout.down(), desc='Move focus down' ),
    Key( [ mod ], 'k', lazy.layout.up(), desc='Move focus up' ),
    Key( [ mod ], 'space', lazy.layout.next(), desc='Move window focus to other window' ),

    Key( [ mod, 'shift' ], 'h', lazy.layout.shuffle_left(), desc='Move window to the left' ),
    Key( [ mod, 'shift' ], 'l', lazy.layout.shuffle_right(), desc='Move window to the right' ),
    Key( [ mod, 'shift' ], 'j', lazy.layout.shuffle_down(), desc='Move window down' ),
    Key( [ mod, 'shift' ], 'k', lazy.layout.shuffle_up(), desc='Move window up' ),

    Key( [ mod, 'control' ], 'h', lazy.layout.grow_left(), desc='Grow window to the left' ),
    Key( [ mod, 'control' ], 'l', lazy.layout.grow_right(), desc='Grow window to the right' ),
    Key( [ mod, 'control' ], 'j', lazy.layout.grow_down(), desc='Grow window down' ),
    Key( [ mod, 'control' ], 'k', lazy.layout.grow_up(), desc='Grow window up' ),
    Key( [ mod ], 'n', lazy.layout.normalize(), desc='Reset all window sizes' ),

    Key(
        [ mod, 'shift' ],
        'Return',
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack',
    ),
    Key( [ mod ], 'Return', lazy.spawn( applications[ 'terminal' ] ), desc='Launch terminal' ),
    Key( [ mod ], 'b', lazy.spawn( applications[ 'browser' ] ), desc='Launch Browser' ),
    Key( [ mod ], 'p', lazy.spawn( applications[ 'private_browser' ] ), desc='Launch Browser in Private Mode' ),
    Key( [ mod ], 'e', lazy.spawn( applications[ 'explorer' ] ), desc='Launch File Explorer' ),
    Key( [ mod ], 'v', lazy.spawn( applications[ 'media' ] ), desc='Launch Media Player' ),
    Key( [ mod, 'shift' ], 'c', lazy.spawn( applications[ 'database_client' ] ), desc='Launch Database Client' ),
    Key( [ mod, 'shift' ], 'p', lazy.spawn( applications[ 'tor_browser' ] ), desc='Launch Browser in Tor Mode' ),
    Key( [ mod ], 's', lazy.spawn( applications[ 'screen_shot' ] ), desc='Take a Screenshot' ),
    Key( [ mod ], 'o', lazy.spawn( applications[ 'obs' ] ), desc='Launch OBS' ),
    Key( [ mod ], 'd', lazy.spawn( applications[ 'docker' ] ), desc='Launch Docker' ),
    Key( [ mod, 'shift' ], 'd', lazy.spawn( applications[ 'docker_restart' ] ), desc='Launch Docker' ),

    Key( [ mod ], 'Tab', lazy.next_layout(), desc='Toggle between layouts' ),
    Key( [ mod ], 'w', lazy.window.kill(), desc='Kill focused window' ),
    Key( [ mod, 'control' ], 'r', lazy.reload_config(), desc='Reload the config' ),
    # Key( [ mod, 'control' ], 'q', lazy.shutdown(), desc='Shutdown Qtile' ),
    Key( [ mod ], 'r', lazy.spawncmd(), desc='Spawn a command using a prompt widget' ),
]

groups = [ Group( i ) for i in [
    "   ", "    ", "   ", " 󰌠  ", "   ", "   ", " 󰊢  ", "  ",
] ]

for i, group in enumerate( groups ):
    actual_key = str( i + 1 )
    keys.extend([
        Key(
            [ mod ],
            actual_key, lazy.group[ group.name ].toscreen()
        ),
        Key(
            [ mod, "shift" ],
            actual_key,
            lazy.window.togroup( group.name, switch_group=True )
        )
    ])


layout_config = {
    'border_focus': '#65B741',
    'border_width': 2,
    'margin': 3
}

layouts = [
    layout.Bsp(
        border_focus="#9ccfd8",
        border_normal="#31748f",
        border_width=1, margin=5
    ),
    layout.Max( **layout_config ),
]

widget_defaults = dict(
    # font='CaskaydiaCove NFM Regular',
    font='JetBrainsMono Nerd Font',
    fontsize=18,
    padding=6,
    # background='#4D455D'
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=10,
                ),
                widget.Image(
                    filename="~/.config/qtile/archlinux-icon.svg",
                    scale="False"
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                widget.GroupBox(
                    active="#ffffff",
                    rounded=False,
                    highlight_color="#c4a7e7",
                    highlight_method="line",
                    borderwidth=0
                ),
                widget.WindowName(
                    foreground="#eb6f92",
                    markup=True,
                    font="CodeNewRoman Nerd Font",
                    fontsize=15,
                    max_chars=63
                ),
                widget.TextBox(
                    text='',
                    background="#232136",
                    foreground="#f6c177",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text=' ',
                    background="#f6c177",
                    foreground="#191724",
                    padding=7
                ),
                widget.CurrentLayout(
                    background="#f6c177",
                    foreground="#191724"
                ),
                widget.TextBox(
                    text='',
                    background="#f6c177",
                    foreground="#e0def4",
                    padding=0,
                    fontsize=42
                ),
                widget.CPU(
                    background="#e0def4",
                    foreground="191724",
                    format="󰘚 {load_percent}%"
                ),
                widget.TextBox(
                    text='',
                    foreground="#eb6f92",
                    background="#e0def4",
                    padding=0,
                    fontsize=42
                ),
                widget.Memory(
                    format="{MemUsed: .0f}{mm}",
                    background="#eb6f92",
                    foreground="#191724",
                    interval=1.0
                ),
                widget.TextBox(
                    text='',
                    background="#eb6f92",
                    foreground="#9ccfd8",
                    padding=0,
                    fontsize=42
                ),
                widget.Net(
                    interface="enp0s31f6",
                    format=" {interface}: {down} ↓↑ {up}",
                    background="#9ccfd8",
                    foreground="#191724",
                    update_interval=1.0
                ),
                widget.TextBox(
                    text='',
                    background="#9ccfd8",
                    foreground="#c4a7e7",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text='',
                    background="#c4a7e7",
                    foreground="#191724",
                    padding=7
                ),
                widget.Clock(
                    background="#c4a7e7",
                    foreground="#191724",
                    format="%H:%M - %d/%m/%Y",
                    update_interval=60.0
                ),
                widget.TextBox(
                    text='',
                    background="#c4a7e7",
                    foreground="#232136",
                    padding=0,
                    fontsize=42
                ),
                widget.Volume(
                    foreground="#e0def4",
                    fmt=" {}"
                ),
                widget.Systray(),
            ],
            25,
            background="#232136",
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active="#ffffff",
                    rounded=False,
                    highlight_color="#c4a7e7",
                    highlight_method="line",
                    borderwidth=0
                ),
                widget.WindowName(
                    foreground="#eb6f92",
                    markup=True,
                    font="CodeNewRoman Nerd Font",
                    fontsize=15,
                ),
                widget.TextBox(
                    text='',
                    foreground="#e0def4",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text=' ',
                    background="#e0def4",
                    foreground="#191724",
                    padding=2
                ),
                widget.CheckUpdates(
                    update_interval=18000,
                    display_format="{updates}",
                    colour_have_updates="#191724",
                    background="#e0def8"
                ),
                widget.TextBox(
                    text='',
                    background="#e0def8",
                    foreground="#c4a7e7",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text='',
                    background="#c4a7e7",
                    foreground="#191724",
                    padding=7
                ),
                widget.Clock(
                    background="#c4a7e7",
                    foreground="#191724",
                    format="%H:%M",
                    update_interval=60.0
                ),
            ],
            25,
            background="#232136",
        ),
    ),

]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "LG3D"

