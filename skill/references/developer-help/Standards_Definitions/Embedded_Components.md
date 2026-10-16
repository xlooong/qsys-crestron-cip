# Embedded Components
> 来源: https://help.qsys.com/DeveloperHelp/Content/Standards_Definitions/Embedded_Components.htm

Most Audio components and some Control components can be embedded in a Plugin via the GetComponents(props) reserved function. You can interact with these components via their controls and audio pins. Other types of pins are not supported, such as Control, USB, Mediacast, or Dataport pins.

> **Note:** Inventory components cannot be embedded in a plugin.

> **Tip:** Go to Storing Secrets in Plugins to see an example of storing Strings in an Embedded Component.

## Accessing Controls of an Embedded Component

## Finding Control Names

The best tool to obtain the correct control names for any component is the "Component Controls" pane in Q-SYS Designer Software (QDS).

To show this pane, select Tools > View Component Controls Info. You then select any component in your design.

## Accessing Embedded Components during Runtime

The name you assign to the component will be added to the global table for access of that component during the runtime. For example, if you defined a crossfader with the name of Xfade, you would use Xfade["crossfade.to.B"].Boolean = true to execute a crossfade.

If you create components using a loop, you can access them via the global table. For example:


```
 
-- Part of GetComponents(props)

 
for
 x = 
1
, (props[
"Output Count"
].Value) 
do

  
table
.
insert
(

    components,

    {

      Name = 
"XFader"
 .. x,

      Type = 
"crossfader"
,

      Properties = {

        [
"multi_channel_type"
] = multiTypeIndex,

        [
"multi_channel_count"
] = props[
"Count"
].Value

      }

    }

  )

 
end

-- Part of runtime

local
 XFaders = {}

for
 i = 
1
, Properties[
"Output Count"
].Value 
do

  
table
.
insert
(XFaders, 
_G
[
"XFader"
 .. i])

end
```

> **Tip:** Remember that Properties are configured in Design Time and are read-only during Runtime.

## Supported Components

## Audio Components

## Audio Players

> **Note:** Embedded audio components will not pass audio if all their input and output pins are referenced in GetWiring().

## Audio Player (audio_file_player)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Track Count | n_channels | integer | 2 | 1 to 128 | This affects the number of Audio Player Tracks counted against a design |
| Player Name | player_name | string | no default value |  | This is for aesthetics in designer and not required in this case |
| Playlist Capable | b_playlist | boolean | false |  |  |

## Bin Loop (binloop)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Output Count | n_outputs | integer | 1 | 0 to 128 | This affects the number of Audio Player Tracks counted against a design. |

## Loop Player (loop_player)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Time Source | io_config | integer | 0 | 0 - GPS 1 - LTC 2 - None 3 - GPS External 4 - PTP |  |
| Frame Rate(fps) | frame_rate | float | 29.97002997003 | 29.97002997003 30 25 24 | Only used when Time Source is set to LTC |
| Output Count | n_channels | integer | 8 | 1 to 128 | This affects the number of Audio Player Tracks counted against a design |
| Buffer Adjustment | buffer_adjustment | float | 1 | 0.1 to 1 |  |
| User UTC | utc_offset_rw | boolean | false |  | Only used when Time Source is set to PTP |

## Audio Recorder (audio_file_recorder2)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Track Count | n_channels | integer | 2 | 1 to 4 | This affects the number of Audio Recorder Channels counted against a design |

## Cinema

## Active Matrix Surround Decoder (active_matrix_surround_decoder)

Component Help

This component has no properties.

## MDA Player (mda_player)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| File Source | file_source | integer | 1 | 0 - Local 1 - HTTP |  |
| Output Count | n_channels | integer | 8 | 1 to 128 |  |

## Cinema Pink Noise Generator (pink_cinema)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## Crossfader (crossfader)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## Crossover (crossover)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Max Slope | max_slope | integer | 48 | 12, 24, 36, 48, 60, 72, 84, 96 | Measured in dB / Octave |
| Band Count | n_bands | integer | 3 | 2 - 6 | Changing this property will change audio pin and control names. 2 - High, Low 3 - High, Mid, Low 4 - High, Mid-High, Mid, Low 5 - High, Mid-High, Mid, Low, Sub 6 - High, Mid-High, Mid, Low-Mid, Low, Sub |
| Highpass Low Band | highpass_low_band | boolean | false |  |  |
| Lowpass High Band | lowpass_high_band | boolean | false |  |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## Delay (delay)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Tap Count | n_taps | integer | 1 | 1 - 512 |  |
| Max Delay (Seconds) | max_delay | float | 0.5 | 0.001 - 60 |  |
| Delay Type | delay_type | integer | 0 | 0 - Standard 1 - Fractional 2 - Crossfaded |  |
| Tap Gain | linear_tap_gain | integer | 0 | 0 - Standard 1 - Linear 2 - X-Fade -3dB 3 - X-Fade -6dB |  |
| Distance Controls | distance_ctrls | boolean | false |  |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## Dynamics

## Automatic Gain Control (leveler)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Side Chain Input | b_has_sidechain | boolean | false |  |  |
| Detector Time | detector_time | float | 0.005 | 0 - Use Control 0.005 - 5ms 0.01 - 10ms 0.02 - 20ms 0.05 - 50ms |  |
| Bypass Gain Meter | bypass_mode | integer | 0 | 0 - Active 1 - Inactive |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## Compressor (compressor)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Side Chain Input | b_has_sidechain | boolean | false |  |  |
| Detector Time | detector_time | float | 0.005 | 0 - Use Control 0.005 - 5ms 0.01 - 10ms 0.02 - 20ms 0.05 - 50ms |  |
| Bypass Gain Meter | bypass_mode | integer | 0 | 0 - Active 1 - Inactive |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## Continuous Ambient Compensator (ambient_compensator_continuous_2)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Audio Bandwidth | subsample_factor | integer | 8 | 1 - 20kHz 2 - 10kHz 4 - 5kHz 8 - 2.5kHz 16 - 1.25kHz |  |
| Microphone Filter | microphone_filter | boolean | true |  |  |
| Relative Venue Size | relative_venue_size | integer | 4 | 1 - 10 |  |
| Detector Time Constant | detector_time | integer | 1 | 0 - Use Control 1 - 1s 10 - 10s 60 - 60s |  |

## Expander (expander)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Side Chain Input | b_has_sidechain | boolean | false |  |  |
| Detector Time | detector_time | float | 0.005 | 0 - Use Control 0.005 - 5ms 0.01 - 10ms 0.02 - 20ms 0.05 - 50ms |  |
| Bypass Gain Meter | bypass_mode | integer | 0 | 0 - Active 1 - Inactive |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## Gate (gate)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Side Chain Input | b_has_sidechain | boolean | false |  |  |
| Detector Time | detector_time | float | 0.005 | 0 - Use Control 0.005 - 5ms 0.01 - 10ms 0.02 - 20ms 0.05 - 50ms |  |
| Bypass Gain Meter | bypass_mode | integer | 0 | 0 - Active 1 - Inactive |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## Gated Ambient Compensator (ambient_compensator_gated_2)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Microphone Filter | microphone_filter | boolean | true |  |  |

## Peak Limiter (limiter_peak)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Side Chain Input | b_has_sidechain | boolean | false |  |  |
| Detector Time | detector_time | float | 0.005 | 0 - Use Control 0.005 - 5ms 0.01 - 10ms 0.02 - 20ms 0.05 - 50ms |  |
| Bypass Gain Meter | bypass_mode | integer | 0 | 0 - Active 1 - Inactive |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## Priority Ducker (priority_ducker)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Channels | n_channels | integer | 8 | 1 - 512 |  |
| Detector Time | detector_time | float | 0.005 | 0 - Use Control 0.005 - 5ms 0.01 - 10ms 0.02 - 20ms 0.05 - 50ms |  |
| Bypass Gain Meter | bypass_mode | integer | 0 | 0 - Active 1 - Inactive |  |

## Effects

## Auto-Pan Effect (effect_autopan)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| I/O Configuration | io_config | integer | 0 | 0 - Mono In/Stereo Out 1 - Stereo In/Stereo Out |  |

## Chorus Effect (effect_chorus)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| I/O Configuration | io_config | integer | 0 | 0 - Mono In/Mono Out 1 - Mono In/Stereo Out 2 - Stereo In/Stereo Out |  |
| Max Delay (Seconds) | max_delay | 0.1 | .001 - 1 |  |  |

## Delay Effect (effect_delay)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| I/O Configuration | io_config | integer | 0 | 0 - Mono In/Mono Out 1 - Mono In/Stereo Out 2 - Stereo In/Stereo Out |  |
| Max Delay (Seconds) | max_delay | 1 | .001 - 60 |  |  |

## Flanger Effect (effect_flange)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| I/O Configuration | io_config | integer | 0 | 0 - Mono In/Mono Out 1 - Mono In/Stereo Out 2 - Stereo In/Stereo Out |  |
| Max Delay (Seconds) | max_delay | 0.1 | .001 - 1 |  |  |

## Pitch Shifter Effect (effect_pitch)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| I/O Configuration | io_config | integer | 0 | 0 - Mono In/Mono Out 1 - Mono In/Stereo Out 2 - Stereo In/Stereo Out |  |
| Max Delay (ms) | max_delay | 1 | 1 - 100 |  |  |

## Reverb Effect (effect_reverb)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| I/O Configuration | io_config | integer | 0 | 0 - Mono In/Stereo Out 1 - Stereo In/Stereo Out |  |
| Reverb Type | reverb_type | integer | 0 | 0 - Lush 1 - Dense |  |

## Tremolo Effect (effect_tremolo)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| I/O Configuration | io_config | integer | 0 | 0 - Mono In/Mono Out 1 - Mono In/Stereo Out 2 - Stereo In/Stereo Out |  |

## Equalizers and Filters

## All-Pass Filter (filter_allpass)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Filter Order | filter_order | integer | 2 | 1 - First order 2 - Second Order |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## Band-Pass Filter (filter_bandpass)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## Band-Stop Filter (filter_bandstop)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## Dual-Shelf Equalizer (equalizer_shelving_dual)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Filter Slope | filter_slope | integer | 12 | 6 - 6dB/Octave 12 - 12dB/Octave |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## FIR Custom Filter (filter_fir)

Component Help

> **Note:** Coefficients can't be loaded in from a file while embedded but they can be loaded in via the JSON String control. See the above Component Help file for more information and an example.

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Coefficient Count | n_taps | integer | 384 | 4 - 16384 | Ensure that the Coefficient Count equals the number of coefficients (FIR taps) in your FIR coefficients configuration |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## FIR High-Pass Filter (filter_highpass_fir)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Transition Bandwidth | bandwidth | float | 1 | 1 - 1 Octave 0.5 - 1/2 Octave 0.25 - 1/4 Octave | Custom is not supported as an embedded component |
| Stopband Attenuation | attenuation | integer | 100 | 40, 60, 80, 100 | Custom is not supported as an embedded component |
| Phase Response | phase_type | integer | 1 | 0 - Minimum Phase 1 - Linear Phase |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## FIR Low-Pass Filter (filter_lowpass_fir)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Transition Bandwidth | bandwidth | float | 1 | 1 - 1 Octave 0.5 - 1/2 Octave 0.25 - 1/4 Octave | Custom is not supported as an embedded component |
| Stopband Attenuation | attenuation | integer | 100 | 40, 60, 80, 100 | Custom is not supported as an embedded component |
| Phase Response | phase_type | integer | 1 | 0 - Minimum Phase 1 - Linear Phase |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## Flattop Graphic Equalizer (equalizer_graphic_flattop)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Band Count | n_bands | integer | 11 | 6, 11, 16, 31, 61 |  |
| Transition Bandwidth | transition_bandwidth | float | 0.0833333333333333 | 0.0833333333333333, 0.166666666666667, 0.333333333333333, 0.5, 1 | Measured in fraction of an Octave Example: 0.0833333333333333 = 1/12 Octave |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## Flattop Parametric Equalizer (equalizer_parametric_flattop)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Band Count | n_bands | integer | 4 | 1 - 32 |  |
| Minimum Transition Bandwidth | minimum_transition_bandwidth | float | 0.0833333333333333 | 0.0833333333333333, 0.166666666666667, 0.333333333333333, 0.5, 1 | Measured in fraction of an Octave Example: 0.0833333333333333 = 1/12 Octave |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## Graphic Equalizer (equalizer_graphic)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Band Count | n_bands | integer | 11 | 6, 11, 16, 31, 61 |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## High-Pass Filter (filter_highpass)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Max Slope | max_slope | integer | 24 | 12, 24, 36, 48, 60, 72, 84, 96 | Measured in dB / Octave |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## High-Shelf Equalizer (equalizer_shelving_high)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Filter Slope | filter_slope | integer | 12 | 6 - 6dB/Octave 12 - 12dB/Octave |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## IIR Custom Filter (filter_IIR)

Component Help

> **Note:** Coefficients can't be loaded in from a file while embedded but they can be loaded in via the JSON String control. See the above Component Help file for more information and an example.

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Section Count | n_sections | integer | 1 | 1 - 256 | The quantity defined here should match the number of coefficients passed in |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## Low-Pass Filter (filter_lowpass)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Max Slope | max_slope | integer | 24 | 12, 24, 36, 48, 60, 72, 84, 96 | Measured in dB / Octave |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## Low-Shelf Equalizer (equalizer_shelving_low)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Filter Slope | filter_slope | integer | 12 | 6 - 6dB/Octave 12 - 12dB/Octave |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## Notch Feedback Controller (feedback_canceler_notch)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Max Filter Count | max_filter_count | integer | 32 | 8 - 32 |  |

## Notch Filter (filter_notch)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## Parametric Equalizer(equalizer_parametric)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Band Count | n_bands | integer | 4 | 1 - 32 |  |
| Bandwidth or Q-Factor | bandwidth_q_factor | integer | 0 | 0 - Bandwidth 1 - Q-Factor 2 - Both |  |
| High Precision | high_precision | boolean | false |  |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## Weighting Filter (filter_weighting)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Weighting | type | integer | 1 | 1 - ANSI S1.42 A 2 - ANSI S1.42 C |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response_panel_enabled | boolean | true |  |  |
| Size | response_panel_size | integer | 1 | 1 - Small 2 - Medium 3 - Large | Only used when Enable is set to true |

## Gain (gain)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Max Gain (dB) | max_gain | integer | 20 | -100 - 20 |  |
| Min Gain (dB) | min_gain | integer | -100 | -100 - 20 |  |
| Enable Ramp Controls | enable_stepper | boolean | false |  |  |
| Mode | step_mode | integer | 0 | 0 - Continuous 1 - Discrete | Only Used when Enable Ramp Controls is set to true |
| Number of Steps | num_steps | integer | 8 | 3 - 100 | Only Used when Enable Ramp Controls is set to true and Mode is set to Discrete |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## Gain Ramp (ramp)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## Meters

## Level Meter (meter2)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Meter Type | meter_type | integer | 1 | 1 - True Peak/RMS 2 - Peak Program 3 - True Peak/RMS - dB-Linear |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## LKFS Meter (BETA) (meter_LKFS)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Input Type | n_channels | integer | 1 | 1 - Mono 2 - Stereo 3 - LCR 5 - 5.1 Surround 7 - 7.1 Surround |  |

## SPL/Leq meter (meter_SPL)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Meter Type | meter_type | integer | 1 | 1 - SPL 2 - Leq |  |
| Frequency Weighting | type | integer | 2 | 1 - Linear 2 - ANSI S1.42 A 3 - ANSI S1.42 C |  |
| Level Range | level_offset | integer | 20 | 0 - 0-100dB 10 - 10-110dB 20 - 20-120dB 40 - 40-140dB |  |

## Mixers

## Delay Matrix Mixer (delay_matrix)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Input Count | n_inputs | integer | 8 | 1 - 512 |  |
| Output Count | n_outputs | integer | 8 | 1 - 512 |  |
| Max Delay (Seconds) | max_delay | float | 0.5 | 0.001 - 60 |  |
| Delay type | delay_type | integer | 0 | 0 - Standard 1 - Fractional 2 - Crossfaded |  |
| Gain Type | linear_gain | integer | 0 | 0 - Standard 1 - Linear 2 - X-Fade -3dB 3 - X-Fade -6dB |  |
| Label Controls | label_controls | boolean | false |  |  |
| Input Gain | input_gain | boolean | false |  |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## Gain-Sharing Automatic Mic Mixer (auto_mixer)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Channels | n_channels | integer | 8 | 2 - 512 |  |
| Outputs | output_choice | integer | 3 | 1 - Mix Only 2 - Channel Only 3 - Mix and Channel |  |
| Side-Cain Filter | sidechain_filter | boolean | false |  |  |
| Detector Time | detector_time | float | 0.005 | 0 - Use Control 0.005 - 5ms 0.01 - 10ms 0.02 - 20ms 0.05 - 50ms |  |

## Gating Automatic Mic Mixers

## Gating Automatic Mic Mixer (Legacy) (auto_mixer_gated)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Channels | n_channels | integer | 8 | 2 - 512 |  |
| Outputs | output_choice | integer | 3 | 1 - Mix Only 2 - Channel Only 3 - Mix and Channel |  |
| Side-Cain Filter | sidechain_filter | boolean | false |  |  |
| Show Advanced Controls | show_advanced_controls | boolean | false |  |  |

## Gating Automatic Mic Mixer (auto_mixer_gating_adaptive)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Channels | n_channels | integer | 8 | 2 - 512 |  |
| Outputs | output_choice | integer | 3 | 1 - Mix Only 2 - Channel Only 3 - Mix and Channel |  |
| Side-Cain Filter | sidechain_filter | boolean | false |  |  |
| Show Advanced Controls | show_advanced_controls | boolean | false |  |  |

## Matrix Mixer (mixer)

Component Help

> **Note:** Max size of the Mixer is 512x512 channels. See the Component Help for more details and limitations.

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Mono | n_inputs | integer | 8 | 1 - 512* | Number of total input channels between mono and stereo must be equal or less than 512 |
| Stereo | n_stereo_inputs | integer | 0 | 1 - 256* | Number of total input channels between mono and stereo must be equal or less than 512 |
| Mono | n_outputs | integer | 8 | 1 - 512* | Number of total output channels between mono and stereo must be equal or less than 512 |
| Stereo | n_stereo_outputs | integer | 0 | 1 - 256* | Number of total output channels between mono and stereo must be equal or less than 512 |
| Input Bank Size | input_bank_strategy | integer | 1 | 0 - Not Banked 1 - Automatic 2 - 1 Channel 3 - 16 Channel 4 - 32 Channel 5 - Custom |  |
|  | input_bank_custom | integer | 32 | 1 - 512 | Only used when Input bank Size is set to Custom |
| Output Bank Size | output_bank_strategy | integer | 1 | 0 - Not Banked 1 - Automatic 2 - 1 Channel 3 - 16 Channel 4 - 32 Channel 5 - Custom |  |
|  | output_bank_custom | integer | 32 | 1 - 512 | Only used when Output bank Size is set to Custom |
| Cue Bus Count | n_cues | integer | 0 | 0 - 511* | Each Cue counts as an output for counting against the max 512 output channels |
| VCA Groups | n_vca_groups | integer | 0 | 0 - 16 |  |
| 2-D Matrix Panner | matrix_panner | boolean | false |  | Available only when there are no stereo inputs or outputs |
| Panner Normalization | spatializer_normalization | integer | 0 | 0 - Constant Voltage 1 - Constant Power | Only used when 2-D Matrix Panner is set to true |
| Pan Controls | pan_strategy | integer | 1 | 0 - No Pan Controls 1 - Pan Per Input 2 - Pan Per Crosspoint | Only can be used when at least one of the Input or Output channels is Stereo |
| Label Controls | label_controls | boolean | true |  |  |
| Crosspoint Mute Controls | crosspoint_mute | boolean | false |  | Only used when 2-D Matrix Panner is set to false |
| Crosspoint Solo Controls | crosspoint_solo | boolean | false |  | Only used when 2-D Matrix Panner is set to false |
| Crosspoint Gain Type | crosspoint_gain_type | integer | 0 | 0 - Standard 1 - X-Fade -3dB 2 - X-Fade -6dB |  |

## Room Combiner (room_combiner)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Rooms | n_rooms | integer | 8 | 2 - 256 |  |
| Walls | n_walls | integer | 8 | 1 - 256 |  |
| Channels | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo |  |
| BGM Inputs | n_bgm | integer | 0 | 0 - 32 |  |

## Router (router_with_output)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Input Count | n_inputs | integer | 8 | 1 - 1024 |  |
| Output Count | n_outputs | integer | 8 | 1 - 1024 |  |
| Selection Controls | select_strategy | integer | 2 | 0 - Knobs 1 - Combo Boxes 2 - Crosspoint Buttons |  |
| Selection Mode | output_select | integer | 0 | 0 - Source 1 - Destination |  |
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## Signal Presence (signal_presence)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## System Mute (system_mute)

Component Help

This component has no properties.

## Test and Measurement

## IO Monitor (io_monitor)

Component Help

This component has no properties.

## Pink Noise Generator (pink)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## Responsalyzer (responsalyzer)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| RTA Bandwidth | n_bands | integer | 121 | 11 - 1 Octave 31 - 1/3 Octave 61 - 1/6 Octave 121 - 1/12 Octave 241 - 1/24 Octave |  |
| FFT Size | n_bins | integer | 16384 | 512, 1024, 2048, 4096, 8196, 16384, 32768, 65536 |  |
| Time Constant Controls | time_constant_controls_name | boolean | false |  |  |

## RTA - Band-Pass (rta_bandpass)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Bandwidth | n_bands | integer | 31 | 11 - 1 Octave 31 - 1/3 Octave 61 - 1/6 Octave 121 - 1/12 Octave 241 - 1/24 Octave |  |

## Sine Generator (sine)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## White Noise Generator (white)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Type | multi_channel_type | integer | 1 | 1 - Mono 2 - Stereo 3 - Multi-channel |  |
| Count | multi_channel_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

## Timecode

## SMPTE LTC Generator (linear_timecode_encoder)

Component Help

This component has no properties.

## SMPTE LTC Reader (linear_timecode_decoder)

Component Help

This component has no properties.

## Control Components

## Astronomical Clock (sun)

Component Help

This component has no properties.

## Blinking LED (blinker)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Assign component to | io_assignment | integer | 0 | 0 - Core 1 - I/O Frame | I/O Frame is not supported as an Embedded Component |

## Color Picker (color_picker)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Color Picker Size | color_picker_size | integer | 256 | 160 - 512 | This is for aesthetics in designer and not required in this case |

## Contact List (contact_list)

Component Help

This component has no properties.

## Custom Controls (custom_controls)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Type | type_<1-10> | integer | 0 | 0 - None 1 - Level fader w/taper (dB ) 2 - Level knob (dB) 3 - Frequency knob (Hz) 4 - Time Knob (seconds) 5 - Generic float knob 6 - Generic Integer knob 7 - Mute button 8 - Toggle button 9 - Trigger button 10 - Percent knob 11 - Position knob 12 - Pan knob 13 - Text edit 14 - Text display 15 - LED 16 - Meter 17 - Momentary button 18 - Distance knob (meters) 19 - Status Display 20 - Hexadecimal knob 21 - Time knob | For more information about each type see below |
| Count | count_<1-10> | integer | 1 | 1-256 |  |
| Customize range | range_custom_<1-10> | boolean | false |  | See Table Below for Types that support Custom ranges |
| Minimum | range_minimum_<1-10> | integer | See Table Below | See Table Below | Only used when Customize range is set to true |
| Maximum | range_maximum_<1-10> | integer | See Table Below | See Table Below | Only used when Customize range is set to true |

| Type | Control Name | Default Range | Supports Custom Range | Custom Range | Notes |
|---|---|---|---|---|---|
| Level fader w/taper (dB ) | fader.1 | -100 - 20 | No |  |  |
| Level knob (dB) | level.1 | -100 - 20 | Yes | -100 - 100 |  |
| Frequency knob (Hz) | frequency.1 | 10 - 20000 | Yes | 0.1 - 20000 |  |
| Time Knob (seconds) | time.1 | 0 - 1 | Yes | 0 - 86400 | Can't use at same time as Time knob |
| Generic float knob | float.1 | 0 - 1 | Yes | -1000000000 - 1000000000 |  |
| Generic Integer knob | integer | 0 - 1 | Yes | -16777216 - 16777216 |  |
| Mute button | mute.1 |  | No |  |  |
| Toggle button | toggle.1 |  | No |  |  |
| Trigger button | trigger.1 |  | No |  |  |
| Percent knob | percent.1 | 0 - 100 | No |  |  |
| Position knob | position.1 | 0 - 1 | No |  |  |
| Pan knob | pan.1 | L100 - R100 -1 - 1 | No |  | Center Value is shown as C with a Value of 0 |
| Text edit | text.1 |  | No |  |  |
| Text display | text.display.1 |  | No |  |  |
| LED | led.1 |  | No |  |  |
| Meter | meter.1 | -120 - 20 | No |  |  |
| Momentary button | momentary.1 |  | No |  |  |
| Distance knob (meters) | distance.1 | 0 - 100 | Yes | 0 - 999 |  |
| Status Display | status.1 |  | No |  |  |
| Hexadecimal knob | hexadecimal.1 | 0 - 8 0x0 - 0xFF | Yes | 0 - 24 0x0 - 0xFFFFFF | Any bits below the minimum results in a high bit. for example a range of 3-8 results in 0x3 - 0xFF |
| Time knob | time.1 | 0 - 1 | Yes | 0 - 86399 | Can't use at same time as Time knob (seconds) |

## Date/Time (date_time)

Component Help

This component has no properties.

## E-mailer (email)

Component Help

This component has no properties.

## Event Log (event_log)

Component Help

This component has no properties.

## Event Logger (event_logger)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Arg Count | Args | integer | 1 | 0 - 16 |  |

## Flip-Flop (flip_flop)

Component Help

This component has no properties.

## GPS Info (gps_info)

Component Help

This component has no properties.

## LFO (control_lfo)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Type | lfo_type | integer | 0 | 0 - Generic (Percentage) 1 - Level Modulator 2 - Frequency Modulator |  |

## PIN Pad (pinpad_2)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| PIN Count | n_pins | integer | 1 | 0 - 16 |  |

## Press and Hold (press_n_hold)

Component Help

This component has no properties.

## Selector (selector)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Selection Count | num_sel | integer | 4 | 2 - 64 |  |

## UCI Layer Controller (uci_layer_controller)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| UCI | uci | string |  |  |  |
| Page | page | string |  |  |  |
| Is Shared | is_shared | boolean | false |  |  |

## UCI Style Controller (uci_style_controller)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| UCI | uci | string |  |  |  |

## Value Stepper (stepper)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| Control Type | control_type | integer | 2 | 0 - Gain 1 - percentage 3 - Integer |  |
| Mode | gain_mode | integer | 0 | 0 - Continuous 1 - Discrete | Only used when Control Type is set to Gain |
| Number of Steps | num_steps | integer | 8 | 3 - 100 | Only used when Control Type is set to Gain and Mode is set to Discrete, or when Control Type is set to Integer |
| Max Gain (dB) | max_gain | integer | 20 | -100 - 20 | Only used when Control Type is set to Gain |
| Min Gain (dB) | min_gain | integer | -100 | -100 - 20 | Only used when Control Type is set to Gain |

## Monitor Components

## Ping (ping)

Component Help

This component has no properties.

## SNMP Query (snmp_query)

Component Help

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
|---|---|---|---|---|---|
| OID Count | snmp_num_oid | integer | 1 | 1 - 16 |  |
| Version | snmp_version | integer | 0 | 0 - v2c 1 - v3 |  |
