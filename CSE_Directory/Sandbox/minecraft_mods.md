# Minecraft Mods

## Overview

There are thousands or even tens of thousands of minecraft mods available. These range from small mods that tweak a part of the game that only occurs in the rarest of scenarios to mods that completly overhaul the game as it is. Additionally there are different mods made for the different mod loaders. While most big mods are on both or at least have a port, the choice of mod loader can be just as important as the mods themselves.

The focus of this mod list is to improve vanilla minecraft in a way that maximizes the potential of what minecraft can do while not deviating away from the vanilla feel. Additionally these mods are focused towards the survival aspect of the game with an emphasis on balence for hardcore play.

## Mod loader: Quilt

This choice is made to take advantage of the vast perfomance mods from the Fabric mod loader while additionally utilizing the mods that are quilt specific. As such there are some core mods that can not be gone without.

| Name                                                                                          | Type | Description         | Confidence |
| --------------------------------------------------------------------------------------------- | ---- | ------------------- | ---------- |
| [Quilted Fabric API (QFAPI) / Quilt Standard Libraries (QSL)](https://modrinth.com/mod/qsl)   | Mod  | Core Library        | xxxxxxxxxx |
| [Quilt Kotlin Libraries (QKL)](https://modrinth.com/mod/qkl)                                  | Mod  | Library wrapper     | xxxxxxxxxx |
| [Mod Menu](https://modrinth.com/mod/modmenu)                                                  | Mod  | In game mod access  | xxxxxxxxxx |

## API and Config Libraries

As with any software development, in order to facilitate the development of meaningful features, common libraries reduce the amount of work a single developer is required to do. Additionally due to the existence of multiple mod loaders for minecraft, there are extra libraries due to ports from one loader to an other.

### Common Functions and API Libraries
| Name                                                          | Type | Description                                        | Confidence |
| ------------------------------------------------------------- | ---- | -------------------------------------------------- | ---------- |
| [Puzzles Lib](https://modrinth.com/mod/puzzles-lib)           | Mod  | Loader agnostic library                            |            |
| [YUNG's API](https://modrinth.com/mod/yungs-api)              | Mod  | Common functions for YUNG's better structures      |            |
| [Cristel Lib](https://modrinth.com/mod/cristel-lib)           | Mod  | Common functions for WWOO and TAT                  |            |
| [Architectury API](https://modrinth.com/mod/architectury-api) | Mod  | Loader agnostic library                            |            |
| [bad packets](https://modrinth.com/mod/badpackets)            | Mod  | Allows packet messaging between modding platforms  |            |
| [Collective](https://modrinth.com/mod/collective)             | Mod  | Used for all serilum mods                          |            |
| [CreativeCore](https://modrinth.com/mod/creativecore)         | Mod  | Used for all creativemd mods                       |            |
| [Iceberg](https://modrinth.com/mod/iceberg)                   | Mod  | Used for all Grend mods                            |            |
| [Prism](https://modrinth.com/mod/prism-lib)                   | Mod  | Another library for Grend mods                     |            |

### Config Libraries
| Name                                                                      | Type | Description                             | Confidence |
| ------------------------------------------------------------------------- | ---- | --------------------------------------- | ---------- |
| [Cloth Config API](https://modrinth.com/mod/cloth-config)                 | Mod  | Standard Fabric config library          |            |
| [YetAnotherConfigLib](https://modrinth.com/mod/yacl)                      | Mod  | Other popular option for Fabric config  |            |
| [Forge Config API Port](https://modrinth.com/mod/forge-config-api-port)   | Mod  | Port for forge mods                     |            |

## Performance

These mods are a staple of the Fabric ecosystem and drasticly improves the fps, tps, and load-times of minecraft.

| Name                                                                          | Type | Description                                                | Confidence |
| ----------------------------------------------------------------------------- | ---- | ---------------------------------------------------------- | ---------- |
| [ImmediatelyFast](https://modrinth.com/mod/immediatelyfast)                   | Mod  | Speed up rendering of various components                   | xxxxxxxxx  |
| [Concurrent Chunk Management Engine](https://modrinth.com/mod/c2me-fabric)    | Mod  | Better multithreading for chunk generation                 | xxxxxxxxxx |
| [Bobby](https://modrinth.com/mod/bobby)                                       | Mod  | Increases rendering distance on servers                    | xxxxxxxxxx |
| [Starlight (Fabric)](https://modrinth.com/mod/starlight)                      | Mod  | Decreases time to calculate lighting                       | xxxxxxx    |
| [Dynamic FPS](https://modrinth.com/mod/dynamic-fps)                           | Mod  | Gives the GPU a break                                      | xxxxxxxxxx |
| [Enhanced Block Entities](https://modrinth.com/mod/ebe)                       | Mod  | Improves rendering of block entities                       | xxxxxxxxxx |
| [Entity Culling](https://modrinth.com/mod/entityculling)                      | Mod  | Doesn't render entities that aren't visable                | xxxxxxxxxx |
| [FerriteCore](https://modrinth.com/mod/ferrite-core)                          | Mod  | Memory usage optimizations                                 | xxxxxxxxxx |
| [Memory Leak Fix](https://modrinth.com/mod/memoryleakfix)                     | Mod  | Removes memory Leaks                                       | xxxxxxxxxx |
| [Krypton](https://modrinth.com/mod/krypton)                                   | Mod  | Network stack optimizations                                | xxxxxxxxx  |
| [LazyDFU](https://modrinth.com/mod/lazydfu)                                   | Mod  | Only runs the DataFixerUpper if needed                     | xxxxxxxxxx |
| [Lithium](https://modrinth.com/mod/lithium)                                   | Mod  | Massive optimizations to the server execution              | xxxxxxxxxx |
| [More Culling](https://modrinth.com/mod/moreculling)                          | Mod  | Doesn't render things that aren't visable                  | xxxxxxxxxx |
| [Sodium](https://modrinth.com/mod/sodium)                                     | Mod  | massive overhaul to the rendering engine                   | xxxxxxxxxx |
| [Nvidium](https://modrinth.com/mod/nvidium)                                   | Mod  | Takes advantage of Nvidia GPU's architecture               | xxxxxxxxxx |
| [Indium](https://modrinth.com/mod/indium)                                     | Mod  | Fabric rendering API compatability with sodium             | xxxxxxxxx  |
| [Reese's Sodium Options](https://modrinth.com/mod/reeses-sodium-options)      | Mod  | More options plus interaction with other mods              | xxxxxxxxx  |
| [Sodium Extra](https://modrinth.com/mod/sodium-extra)                         | Mod  | More features for Sodium                                   | xxxxxxxxx  |
| [Debugify](https://modrinth.com/mod/debugify)                                 | Mod  | Fixes many bugs including some performance bugs            | xxxxxxxxx  |
| [FastQuit](https://modrinth.com/mod/fastquit)                                 | Mod  | Saves worlds in the background                             | xxxxxxxxxx |
| [Clumps](https://modrinth.com/mod/clumps)                                     | Mod  | Clumps XP orbs together to reduce lag                      | xxxxxxxxxx |
| [Language Reload](https://modrinth.com/mod/language-reload)                   | Mod  | Reduces language load times                                | xxxxxxxxx  |
| [Chunky](https://modrinth.com/mod/chunky)                                     | Mod  | Pre-generate parts of the world                            | xxxxxxxxx  |
| [ThreadTweak](https://modrinth.com/mod/threadtweak)                           | Mod  | Smooths out some threading issues                          | xxxxxxxxx  |
| [No Unused Chunks](https://modrinth.com/mod/no-unused-chunks)                 | Mod  | Conservativly removes unenhabited chunks when optimizing   | xxxxxxxx   |

## Optifine Features

The Optifine client/mod has had a very large impact on the minecraft modding community. Optifine includes a host of features that are quiticential to the look and feel of the game.

### Features

| Name                                                                      | Type | Description                                | Confidence |
| ------------------------------------------------------------------------- | ---- | ------------------------------------------ | ---------- |
| [Puzzle](https://modrinth.com/mod/puzzle)                                 | Mod  | Config and other features of Optifine      | xxxxxxxxxx |
| [Iris](https://modrinth.com/mod/iris)                                     | Mod  | Shader support                             | xxxxxxxxxx |
| [Continuity](https://modrinth.com/mod/continuity)                         | Mod  | Connected textures                         | xxxxxxxxxx |
| [LambDynamicLights](https://modrinth.com/mod/lambdynamiclights)           | Mod  | Adds dynamic lights                        | xxxxxxxxxx |
| [LambdaBetterGrass](https://modrinth.com/mod/lambdabettergrass)           | Mod  | Better grass and snow                      | xxxxxxxxxx |
| [CITResewn](https://modrinth.com/mod/cit-resewn)                          | Mod  | Custom item textures                       | xxxxxxxxxx |
| [Entity Model Features](https://modrinth.com/mod/entity-model-features)   | Mod  | Custom entity models                       | xxxxxxxxxx |
| [Entity Texture Features](https://modrinth.com/mod/entitytexturefeatures) | Mod  | Custom entity textures                     | xxxxxxxxxx |
| [Borderless Mining](https://modrinth.com/mod/borderless-mining)           | Mod  | Borderless window instead of Fullscreen    | xxxxxxxxxx |
| [Zoomify](https://modrinth.com/mod/zoomify)                               | Mod  | Allows zooming in                          | xxxxxxxxxx |
| [Fabrishot](https://modrinth.com/mod/fabrishot)                           | Mod  | 4k Screenshots                             | xxxxxxxxx  |

### Related Shaders and Resource Packs

| Name                                                                                                                  | Type          | Description                               | Confidence |
| --------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------------------------------- | ---------- |
| [BetterVanillaBuilding Overlays](https://modrinth.com/resourcepack/bettervanillabuildingoverlays)                     | Resource Pack | Complete overhaul of most textures        | xxxxxxxxx  |
| [BetterVanillaBuilding](https://modrinth.com/resourcepack/bettervanillabuilding)                                      | Resource Pack | Adds connected textures                   | xxxxxxxxx  |
| [BSL Shaders](https://modrinth.com/shader/bsl-shaders)                                                                | Shader        | Most common shader                        | xxxxxxxxxx |
| [Complementary Shaders - Reimagined](https://modrinth.com/shader/complementary-reimagined)                            | Shader        | Overall well balenced shader              | xxxxxxxxxx |
| [Rethinking Voxels](https://modrinth.com/shader/rethinking-voxels)                                                    | Shader        | Ray tracing feel without ray tracing      | xxxxxxxx   |
| [Fresh Animations](https://modrinth.com/resourcepack/fresh-animations)                                                | Resource Pack | Animations like minecraft promo videos    | xxxxxxxxx  |
| [BetterVanillaBuilding x Fresh Animations](https://modrinth.com/resourcepack/bettervanillabuilding-x-freshanimations) | Resource Pack | Compatability with Fresh Animations       | xxxxxxxxx  |
| [Eating Animation - BetterVanillaBuilding Addon](https://modrinth.com/resourcepack/bvb-eating-animation)              | Resource Pack | Compatability with Eating Animation       | xxxxxxxxx  |
| [Dark GUI - BetterVanillaBuilding addon](https://modrinth.com/resourcepack/dark-gui)                                  | Resource Pack | Dark mode for BVB                         | xxxxxxxxx  |

## Player Interaction, Movement and View

As with any other game, how the player is implemented contributes a lot to the game. Vanilla minecraft shows the first person view as a 2D hand; this can be improved. Many additional features can be added to give a better sense of realism.

Additionally how the player feels when they move and look around the world is just as important. Limiting some features like sitting to only a couple corners of the game limits the freedom of the player.

### Player

| Name                                                                      | Type | Description                                        | Confidence |
| ------------------------------------------------------------------------- | ---- | -------------------------------------------------- | ---------- |
| [First-person Model](https://modrinth.com/mod/first-person-model)         | Mod  | Visable hands and legs                             | xxxxxxxxx  |
| [Not Enough Animations](https://modrinth.com/mod/not-enough-animations)   | Mod  | Better player animations                           | xxxxxxxxxx |
| [3D Skin Layers](https://modrinth.com/mod/3dskinlayers)                   | Mod  | Second layer of players skins are now 3D           | xxxxxxxxxx |
| [Show Me Your Skin!](https://modrinth.com/mod/show-me-your-skin)          | Mod  | Configuable option to make player armor invisable  | xxxxxxxxx  |
| [Eating Animation](https://modrinth.com/mod/eating-animation)             | Mod  | Food is eated piece by piece                       | xxxxxxxxxx |
| [Model Gap Fix](https://modrinth.com/mod/modelfix)                        | Mod  | Fixes the bugged lines in held items               | xxxxxxxxxx |

### Movement

| Name                                          | Type | Description                                    | Confidence |
| --------------------------------------------- | ---- | ---------------------------------------------- | ---------- |
| [Sit](https://modrinth.com/mod/bl4cks-sit)    | Mod  | Allows the player to sit on slabs and chairs   | xxxxxxxxx  |
| [Crawl](https://modrinth.com/mod/crawl)       | Mod  | Allows the player to crawl at any time         | xxxxxxxxxx |

### View

| Name                                                                  | Type | Description                         | Confidence |
| --------------------------------------------------------------------- | ---- | ----------------------------------- | ---------- |
| [Freecam](https://modrinth.com/mod/freecam)                           | Mod  | Creative like camera in survival    | xxxxxxxxxx |
| [Freelook](https://modrinth.com/mod/freelook)                         | Mod  | Turn your head like an owl          | xxxxxxxxxx |
| [Better Third Person](https://modrinth.com/mod/better-third-person)   | Mod  | Makes 3rd person intuitive          | xxxxxxxxxx |

## World Generation, Skybox, and water

The player is always interacting with the environment around them. Minecraft's default world generation has improved with time but can look and feel better. Whether it be better looking moutains and oceans, or more adventurous structures, the player will feel more immersed in their world.

### Overworld
| Name                                                                                      | Type          | Description                                   | Confidence |
| ----------------------------------------------------------------------------------------- | ------------- | --------------------------------------------- | ---------- |
| [Tectonic](https://modrinth.com/datapack/tectonic/versions)                               | Datapack/Mod  | Overhauls the overworld biome formation       | xxxxxxxx   |
| [Reterraforged]()                                                                         | Mod           | Realistic world generation                    | xxxxxxxxx  |
| [William Wythers' Overhauled Overworld](https://modrinth.com/mod/wwoo)                    | Mod           | Overhauls the overworld biome look and feel   | xxxxxxxxx  |
| [Towns and Towers](https://modrinth.com/mod/towns-and-towers)                             | Datapack/Mod  | Adds new villages and pillager structures     | xxxxxxxxx  |
| [Custom Stars](https://www.curseforge.com/minecraft/mc-mods/custom-stars)                 | Mod           | Reworks the stars at night                    | xxxxxxxxx  |
| [Better Clouds](https://modrinth.com/mod/better-clouds)                                   | Mod           | Reworks the clouds                            | xxxxxxxxxx |
| [Cubic Sun & Moon](https://modrinth.com/resourcepack/cubic-sun-moon)                      | Resource Pack | Makes the sun and moon into cubes             | xxxxxxxxx  |
| [YUNG's Better Desert Temples](https://modrinth.com/mod/yungs-better-desert-temples)      | Mod           | Desert temples have puzzles and a boss        | xxxxxxxxx  |
| [YUNG's Better Dungeons](https://modrinth.com/mod/yungs-better-dungeons)                  | Mod           | Not boring dungeons                           | xxxxxxxx   |
| [YUNG's Better Jungle Temples](https://modrinth.com/mod/yungs-better-jungle-temples)      | Mod           | Not boring jungle temples                     | xxxxxxxx   |
| [YUNG's Better Mineshafts](https://modrinth.com/mod/yungs-better-mineshafts)              | Mod           | Mineshaft overhaul                            | xxxxxx     |
| [YUNG's Better Ocean Monuments](https://modrinth.com/mod/yungs-better-ocean-monuments)    | Mod           | Larger monuments and includes a trident       | xxxxxx     |
| [YUNG's Better Strongholds](https://modrinth.com/mod/yungs-better-strongholds)            | Mod           | Stronghold overhaul                           | xxxxxxxx   |
| [YUNG's Better Witch Huts](https://modrinth.com/mod/yungs-better-witch-huts)              | Mod           | Witch hut overhaul                            | xxxxxxxx   |
| [YUNG's Extras](https://modrinth.com/mod/yungs-extras)                                    | Mod           | Adds small ruins and such                     | xxxxxxx    |
| [Snow Under Trees](https://modrinth.com/mod/snow-under-trees-remastered)                  | Mod           | Makes snow generate under trees               | xxxxxxxxxx |
| [BedrockWaters](https://modrinth.com/mod/bedrockwaters)                                   | Mod           | Makes water foggier                           | xxxxxxxxxx |
| [Simple Fog Control](https://modrinth.com/mod/simplefog)                                  | Mod           | Better fog controls                           | xxxxxxxxxx |
| [No World Border](https://modrinth.com/resourcepack/invisible-world-border)               | Resource Pack | The world border gets distracting             | xxxxxxxxx  |

### Nether
| Name                                                                                       | Type | Description                                   | Confidence |
| ------------------------------------------------------------------------------------------ | ---- | --------------------------------------------- | ---------- |
| [Amplified Nether](https://modrinth.com/mod/amplified-nether)                              | Mod  | Taller nether and 3D biomes                   | xxxxxxxx   |
| [YUNG's Better Nether Fortresses](https://modrinth.com/mod/yungs-better-nether-fortresses) | Mod  | More detailed fortresses with a central keep  | xxxxxx     |

### End
| Name                                                                          | Type          | Description                       | Confidence |
| ----------------------------------------------------------------------------- | ------------- | --------------------------------- | ---------- |
| [Nullscape](https://modrinth.com/mod/nullscape)                               | Datapack/Mod  | Not boring end generation         | xxxxxxxx   |
| [YUNG's Better End Island](https://modrinth.com/mod/yungs-better-end-island)  | Mod           | End island structures overhaul    | xxxxxxx    |
| [Better End Sky](https://modrinth.com/mod/better-end-sky)                     | Mod           | End sky is no longer boring       | xxxxxxxxxx |

## Sound

As the player interacts with the world, they will both see and hear the environment. To better immerse the player in the world around them, a sound overhaul is needed.

| Name                                                                          | Type | Description                            | Confidence |
| ----------------------------------------------------------------------------- | ---- | -------------------------------------- | ---------- |
| [AmbientSounds](https://modrinth.com/mod/ambientsounds)                       | Mod  | Adds chirping bird sounds and more     | xxxxxxxxx  |
| [Presence Footsteps](https://modrinth.com/mod/presence-footsteps)             | Mod  | Footsteps make reasonable sounds       | xxxxxxxxx  |
| [Sound Physics Remastered](https://modrinth.com/mod/sound-physics-remastered) | Mod  | Reverb and more from the environment   | xxxxxxxxx  |

## HUD

The player's HUD is how the game conveys important information. While vanilla minecraft does a good job at this, the HUD is not required all the time. Additionally some extra features can be added.

| Name                                                                                                                  | Type          | Description                                       | Confidence |
| --------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------- | ---------- |
| [Auto HUD](https://modrinth.com/mod/autohud)                                                                          | Mod           | Hides the HUD when not needed                     | xxxxxxxxxx |
| [Dynamic Crosshair](https://modrinth.com/mod/dynamiccrosshair)                                                        | Mod           | Conveys information based on possible actions     | xxxxxxxxxx |
| [WTHIT](https://modrinth.com/mod/wthit)                                                                               | Mod           | Shows extra information about the block in view   | xxxxxxxxx  |
| [Detail Armor Bar](https://modrinth.com/mod/detail-armor-bar)                                                         | Mod           | The armor bar displayes the type of armor worn    | xxxxxxxxx  |
| [AppleSkin](https://modrinth.com/mod/appleskin)                                                                       | Mod           | More information about what you're eating         | xxxxxxxxxx |
| [Better Ping Display](https://modrinth.com/mod/better-ping-display-fabric)                                            | Mod           | Shows actual ping value instead of bars           | xxxxxxxxxx |
| [BetterF3](https://modrinth.com/mod/betterf3)                                                                         | Mod           | Makes the F3 screen more readable                 | xxxxxxxxxx |
| [Advancement Plaques](https://modrinth.com/mod/advancement-plaques)                                                   | Mod           | Makes advancements feel like an acomplishment     | xxxxxxxxx  |
| [Embellished Stone (Advancements Plaques)](https://modrinth.com/resourcepack/embellished-stone-advancements-plaques)  | Resource Pack | Reskin for Advancement Plaques                    | xxxxxxxxx  |
| [Beautified Chat](https://modrinth.com/mod/beautified-chat-client)                                                    | Mod           | Reformats chat to have a timestamp                | xxxxxxxxxx |
| [More Chat History](https://modrinth.com/mod/morechathistory)                                                         | Mod           | Chat from a week ago                              | xxxxxxxx   |
| [Enhanced Boss Bars](https://modrinth.com/resourcepack/enhanced-boss-bars)                                            | Resource Pack | No longer just a bar                              | xxxxxxx    |
| [Highlight](https://modrinth.com/mod/highlight)                                                                       | Mod           | outline selected blocks properly                  | xxxxxxxx   |
| [Status Effect Bars](https://modrinth.com/mod/status-effect-bars)                                                     | Mod           | Better display for status effects                 | xxxxxxxxxx |

## Menu

Menus are how users interact with any non-immediate information. Whether this is a players inventory, crafting table, mod config screen, or changing render settings, menues are how players interact with more complex parts of the game.

| Name                                                                                  | Type          | Description                               | Confidence |
| ------------------------------------------------------------------------------------- | ------------- | ----------------------------------------- | ---------- |
| [Blur](https://modrinth.com/mod/blur-fabric)                                          | Mod           | Blurs the background when in a menu       | xxxxxxxxxx |
| [InvMove](https://modrinth.com/mod/invmove)                                           | Mod           | Allows movement while in a menu           | xxxxxxxxxx |
| [Portal GUI](https://modrinth.com/mod/portalgui)                                      | Mod           | You can now open a menu in a portal       | xxxxxxxxxx |
| [Smooth Swapping](https://modrinth.com/mod/smooth-swapping)                           | Mod           | Items no longer teleport                  | xxxxxxxxx  |
| [Shulker Box Tooltip](https://modrinth.com/mod/shulkerboxtooltip)                     | Mod           | View the contents of a shulker box        | xxxxxxxxxx |
| [Better Statistics Screen](https://modrinth.com/mod/better-stats)                     | Mod           | Better interface for statistics           | xxxxxxxxx  |
| [Better Recipe Book](https://modrinth.com/mod/brb)                                    | Mod           | Recipe book for more crafting blocks      | xxxxxxxxx  |
| [Cherished Worlds](https://modrinth.com/mod/cherished-worlds)                         | Mod           | Favorite world to protect them            | xxxxxxxx   |
| [Disable Custom Worlds Advice](https://modrinth.com/mod/dcwa)                         | Mod           | I know what I'm doing                     | xxxxxxxxxx |
| [Legendary Tooltips](https://modrinth.com/mod/legendary-tooltips)                     | Mod           | Legendary items have legendary borders    | xxxxxxxx   |
| [Eclectic Trove](https://modrinth.com/resourcepack/eclectic-trove-legendary-tooltips) | Resource Pack | Reskin for Legendary Tooltips             | xxxxxxxx   |
| [Remove Reloading Screen](https://modrinth.com/mod/rrls)                              | Mod           | Reloading occurs in the background        | xxxxxxxxx  |
| [Screenshot Viewer](https://modrinth.com/mod/screenshot-viewer)                       | Mod           | No more going through the filesystem      | xxxxxxxxxx |

## Particles

Particles can be used to add more movement and activity to a world. Minecraft's particle system is strong but computationally ineffecient; until a particle performance mod arives, the amount should be limited.

| Name                                                          | Type | Description                                     | Confidence |
| ------------------------------------------------------------- | ---- | ----------------------------------------------- | ---------- |
| [Cave Dust](https://modrinth.com/mod/cave-dust)               | Mod  | Adds grey dust particles underground            | xxxxxxxxxx |
| [Effective](https://modrinth.com/mod/effective)               | Mod  | Adds multiple effects plus water splashes       | xxxxxxxx   |
| [Falling Leaves](https://modrinth.com/mod/fallingleaves)      | Mod  | Leaf blocks drop leaves                         | xxxxxxxxxx |
| [Make Bubbles Pop](https://modrinth.com/mod/make_bubbles_pop) | Mod  | Bubbles pop realistically                       | xxxxxxxxx  |
| [Visuality](https://modrinth.com/mod/visuality)               | Mod  | Particles for mobs and environments             | xxxxxxxxx  |
| [Wakes](https://modrinth.com/mod/wakes)                       | Mod  | No particles but similar effect to Effective    | xxxxxxxx   |
| [Particle Rain](https://modrinth.com/mod/particle-rain)       | Mod  | Better weather particles plus some more         | xxx        |

## Vanilla+

As minecraft has been developed over the years, some features have either been overlooked or forgoten. Multiple mods have come to fill in the gaps of the game by changing how minecraft plays while still in a vanilla style.

### Client
| Name                                                      | Type | Description                                 | Confidence |
| --------------------------------------------------------- | ---- | ------------------------------------------- | ---------- |
| [AutoTools](https://modrinth.com/mod/minecraft_autotools) | Mod  | Saves time by automatically switching tools | xxxxxxxxxx |
| [JJElytraSwap](https://modrinth.com/mod/jjelytraswap)     | Mod  | Swap elytra when trying to fly              | xxxxxxxxxx |
| [Realistic Bees](https://modrinth.com/mod/realistic-bees) | Mod  | Bees are smaller                            | xxxxxxxx   |
| [SwingThrough](https://modrinth.com/mod/swingthrough)     | Mod  | Don't let grass get in the way              | xxxxxxxxxx |

### Server
| Name                                                                              | Type      | Description                                       | Confidence |
| --------------------------------------------------------------------------------- | --------- | ------------------------------------------------- | ---------- |
| [track raw statistics](https://vanillatweaks.net/picker/datapacks/)               | Datapack  | Keep track of more player activities              | xxxxxx     |
| [wandering trades](https://vanillatweaks.net/picker/datapacks/)                   | Datapack  | Wandering traders now sell block heads            | xxxxxxxxx  |
| [Better Ladders](https://modrinth.com/mod/better-ladders)                         | Mod       | Ladders can now hang                              | xxxxxxxxxx |
| [Better Totem of Undying](https://modrinth.com/mod/better-totem-of-undying-forge) | Mod       | A totem of undying will always save you           | xxxxxxx    |
| [Bottle Your Xp](https://modrinth.com/mod/bottle-your-xp)                         | Mod       | Crouch with a bottle to extract your xp           | xxxxx      |
| [Bottled Air](https://modrinth.com/mod/bottled-air)                               | Mod       | Empty bottles can be used for air                 | xxxxxxxxxx |
| [ChickensShed](https://modrinth.com/mod/chickensshed)                             | Mod       | Chickens drop feathers                            | xxxxxxxxxx |
| [Configurable Despawn Timer](https://modrinth.com/mod/configurable-despawn-timer) | Mod       | items no longer vanish after 5 minutes            | xxxxxxxx   |
| [Crying Portals](https://modrinth.com/mod/crying-portals)                         | Mod       | Crying obsidian also works for portals            | xxxxx      |
| [Double Doors](https://modrinth.com/mod/double-doors)                             | Mod       | Open both doors at the same time                  | xxxxxx     |
| [Grabby Mobs](https://modrinth.com/mod/grabby-mobs)                               | Mod       | Mobs will always grab items if capable            | xxxxxxxx   |
| [ItemPhysic](https://modrinth.com/mod/itemphysic)                                 | Mod       | Items look like block and sink/float realisticly  | xxxxxxxxxx |
| [Just Mob Heads](https://modrinth.com/mod/just-mob-heads)                         | Mod       | Mobs drop their head                              | xxxxxxxxx  |
| [Keep My Soil Tilled](https://modrinth.com/mod/keep-my-soil-tilled)               | Mod       | Pumpkins don't ruin the tilled soil               | xxxxxx     |
| [Milk All The Mobs](https://modrinth.com/mod/milk-all-the-mobs)                   | Mod       | Why no goat milk? Now you can                     | xxxxxxxxxx |
| [Nutritious Milk](https://modrinth.com/mod/nutritious-milk)                       | Mod       | Milk acts like a food                             | xxxxxxxxx  |
| [No Feather Trample](https://modrinth.com/mod/no-feather-trample)                 | Mod       | Farmland isn't trampled if wearing featherfalling | xxxxxx     |
| [Nyf's Spiders](https://modrinth.com/mod/nyfs-spiders)                            | Mod       | Spiders act like spiders                          | xxxxxxxx   |
| [Overworld Piglins](https://modrinth.com/mod/overworld-piglins)                   | Mod       | Piglins can resist the overworld                  | xxxxxxxxx  |
| [Passive Endermen](https://modrinth.com/mod/passive-endermen)                     | Mod       | Endermen no longer place blocks                   | xxxxxxxx   |
| [Quick Right-Click](https://modrinth.com/mod/quick-right-click)                   | Mod       | You don't need to always place crafting blocks    | xxxxxx     |
| [Replanting Crops](https://modrinth.com/mod/replanting-crops)                     | Mod       | Replant with a hoe                                | xxxxxx     |
| [Shulker Drops Two](https://modrinth.com/mod/shulker-drops-two)                   | Mod       | Shulkers drop both their shells                   | xxxxxxxxx  |
| [Skeleton Horse Spawn](https://modrinth.com/mod/skeleton-horse-spawn)             | Mod       | Skeleton horses spawn naturally                   | xxxxxxxxxx |
| [Zombie Horse Spawn](https://modrinth.com/mod/zombie-horse-spawn)                 | Mod       | Zombie horses spawn naturally                     | xxxxxxxxxx |
| [Smaller Nether Portals](https://modrinth.com/mod/smaller-nether-portals)         | Mod       | Nether portals can be any size                    | xxxxxxx    |
| [Smelting Plus](https://modrinth.com/mod/smelting-plus)                           | Mod       | Melting tools and armor gives more                | xxxxxxxx   |
| [Solid Mobs](https://modrinth.com/mod/solid_mobs)                                 | Mod       | You can't walk through a cow                      | xxxxxxxxxx |
| [Spawn Animations](https://modrinth.com/mod/spawn-animations)                     | Mod       | Mobs no longer poof into existance                | xxxxx      |
| [Stackables](https://modrinth.com/mod/stackables)                                 | Mod       | lets more items stack                             | xxxxxxx    |
| [Thorny Bush Protection](https://modrinth.com/mod/thorny-bush-protection)         | Mod       | Don't get pricked if you have pants               | xxxxxx     |
| [Time & Wind](https://modrinth.com/mod/time-wind)                                 | Mod       | Longer or shorter days                            | xxxxxxxxx  |
| [Universal Bone Meal](https://modrinth.com/mod/universal-bone-meal)               | Mod       | Sugar cane is a plant too                         | xxxxxxxxx  |
| [Village Spawn Point](https://modrinth.com/mod/village-spawn-point)               | Mod       | Start in a village                                | xxxxxxxx   |
| [Villager Names](https://modrinth.com/mod/villager-names-serilum)                 | Mod       | Villagers spawn with names                        | xxxxxxxxx  |


### Recipes

| Name                                                                          | Type | Description                             | Confidence |
| ----------------------------------------------------------------------------- | ---- | --------------------------------------- | ---------- |
| [Chain Armor Recipe](https://modrinth.com/mod/chain-armor-recipe)             | Mod  | Make chain armor with chain             | xxxxxxxxx  |
| [Craft Saddles](https://modrinth.com/mod/craftsaddles)                        | Mod  | Make saddles with leather and such      | xxxxxxxxx  |
| [Name Tag Tweaks](https://modrinth.com/mod/name-tag-tweaks)                   | Mod  | Adds a recipe for name tags             | xxxxxxxxx  |
| [Obtainable End](https://modrinth.com/mod/obtainable-end)                     | Mod  | End portals shouldn't be unobtainable   | xxxxxx     |
| [Village Bell Recipe](https://modrinth.com/mod/village-bell-recipe)           | Mod  | Adds a recipe for bells                 | xxxxxxxxx  |
| [Wool Tweaks](https://modrinth.com/mod/wool-tweaks)                           | Mod  | Recipe for string plus more features    | xxxxx      |
| [Exline's Wool to String](https://modrinth.com/mod/exlines-wool-to-string)    | Mod  | Adds a wool to string recipe            | xxxxxxxxx  |

# External Tools

## Overview

Sometimes Things are better done with external applications; specifically, optimizing worlds and debugging.

| Name                                                      | Description               |
| --------------------------------------------------------- | ------------------------- |
| [MCA Selector](https://github.com/Querz/mcaselector)      | Delete or generate chunks |
| [NBTExplorer](https://github.com/jaquadro/NBTExplorer)    | Debug NBT information     |
| [World Painter](https://www.worldpainter.net/)            | Make your custom worlds   |
