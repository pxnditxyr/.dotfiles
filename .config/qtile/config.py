from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.widget.volume import Volume

mod = "mod4"

applications = {
    'terminal': 'kitty',
    'browser': 'microsoft-edge-dev',
    'private_browser': 'microsoft-edge-dev --inprivate',
    'tor_browser': 'brave-browser-nightly --incognito --tor',
    'obs': 'obs',
    'docker': 'systemctl --user start docker-desktop',
    'docker_restart': 'systemctl --user restart docker-desktop'
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
    Key( [ mod, 'shift' ], 'p', lazy.spawn( applications[ 'tor_browser' ] ), desc='Launch Browser in Tor Mode' ),
    Key( [ mod ], 'o', lazy.spawn( applications[ 'obs' ] ), desc='Launch OBS' ),
    Key( [ mod ], 'd', lazy.spawn( applications[ 'docker' ] ), desc='Launch Docker' ),
    Key( [ mod, 'shift' ], 'd', lazy.spawn( applications[ 'docker_restart' ] ), desc='Launch Docker' ),

    Key( [ mod ], 'Tab', lazy.next_layout(), desc='Toggle between layouts' ),
    Key( [ mod ], 'w', lazy.window.kill(), desc='Kill focused window' ),
    Key( [ mod, 'control' ], 'r', lazy.reload_config(), desc='Reload the config' ),
    Key( [ mod, 'control' ], 'q', lazy.shutdown(), desc='Shutdown Qtile' ),
    Key( [ mod ], 'r', lazy.spawncmd(), desc='Spawn a command using a prompt widget' ),
]

groups = [ Group( i ) for i in '123456789' ]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [ mod ],
                i.name,
                lazy.group[ i.name ].toscreen(),
                desc='Switch to group {}'.format( i.name ),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [ mod, 'shift' ],
                i.name,
                lazy.window.togroup( i.name, switch_group=True ),
                desc='Switch to & move focused window to group {}'.format( i.name ),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, 'shift'], i.name, lazy.window.togroup(i.name),
            #     desc='move focused window to group {}'.format(i.name)),
        ]
    )


layout_config = {
    'border_focus': '#B71375',
    'border_width': 2,
    'margin': 4
}

layouts = [
    layout.Columns( **layout_config ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='CaskaydiaCove NFM Regular',
    fontsize=16,
    padding=10,
    background='#4D455D'
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout( background='#FFDCB6', foreground='#2A2F4F' ),
                widget.GroupBox(
                    background='#FFDCB6',
                    foreground='#FF6D60',
                    active='#C92C6D',
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=2,
                    block_highlight_text_color='#3A98B9',
                    # inactivate='#404040',
                    this_current_screen_border='#FF6D60',
                    disable_drag=True
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ('#ff0000', '#ffffff'),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.TextBox( '🐼 Pxndxs 🐼', foreground='#2A2F4F', background='#FFDCB6' ),
                Volume(
                    background='#3EDBF0',
                    padding=3,
                    update_interval=0.1,
                    emoji=True,
                    mute_command='pactl set-sink-mute @DEFAULT_SINK@ toggle',
                    volume_up_command='pactl set-sink-volume @DEFAULT_SINK@ +5%',
                    volume_down_command='pactl set-sink-volume @DEFAULT_SINK@ -5%',
                ),
                widget.Clock( format='%Y-%m-%d %a %I:%M %p', background='#FFDCB6', foreground='#2A2F4F' ),
                # widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
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

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

