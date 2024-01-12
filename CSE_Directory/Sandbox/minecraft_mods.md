# Minecraft Mods

## Overview

There are thousands or even tens of thousands of minecraft mods available. These range from small mods that tweak a part of the game that only occurs in the rarest of scenarios to mods that completly overhaul the game as it is. Additionally there are different mods made for the different mod loaders. While most big mods are on both or at least have a port, the choice of mod loader can be just as important as the mods themselves.

The focus of this mod list is to improve vanilla minecraft in a way that maximizes the potential of what minecraft can do while not deviating away from the vanilla feel. Additionally these mods are focused towards the survival aspect of the game with an emphasis on balence for hardcore play.

## Mod loader: Quilt

This choice is made to take advantage of the vast perfomance mods from the Fabric mod loader while additionally utilizing the mods that are quilt specific. As such there are some core mods that can not be gone without.

| Name                                                                                          | Type | Description         | Confidence |
| --------------------------------------------------------------------------------------------- | ---- | ------------------- | ---------- |
| [Quilted Fabric API (QFAPI) / Quilt Standard Libraries (QSL)](https://modrinth.com/mod/qsl)   | Mod  | Core Library        | 10/10      |
| [Quilt Kotlin Libraries (QKL)](https://modrinth.com/mod/qkl)                                  | Mod  | Library wrapper     | 10/10      |
| [Mod Menu](https://modrinth.com/mod/modmenu)                                                  | Mod  | In game mod access  | 10/10      |

## API and Config Libraries

As with any software development, in order to facilitate the development of meaningful features, common libraries reduce the amount of work a single developer is required to do. Additionally due to the existence of multiple mod loaders for minecraft, there are extra libraries due to ports from one loader to an other.

### Common Functions and API Libraries
| Name | Type | Description | Confidence |
| - | - | - | - |
| [Puzzles Lib](https://modrinth.com/mod/puzzles-lib) | Mod | Loader agnostic library | TODO |
| [YUNG's API](https://modrinth.com/mod/yungs-api) | Mod | Common functions for YUNG's better structures | TODO |
| [Cristel Lib](https://modrinth.com/mod/cristel-lib) | Mod | Common functions for WWOO and TAT | TODO |
| [Architectury API](https://modrinth.com/mod/architectury-api) | Mod | Loader agnostic library | TODO |
| [bad packets](https://modrinth.com/mod/badpackets) | Mod | Allows packet messaging between modding platforms | TODO |
| [Collective](https://modrinth.com/mod/collective) | Mod | Used for all serilum mods | TODO |
| [CreativeCore](https://modrinth.com/mod/creativecore) | Mod | Used for all creativemd mods | TODO |
| [Iceberg](https://modrinth.com/mod/iceberg) | Mod | Used for all Grend mods | TODO |
| [Prism](https://modrinth.com/mod/prism-lib) | Mod | Another library for Grend mods | TODO |

### Config Libraries
| Name | Type | Description | Confidence |
| - | - | - | - |
| [Cloth Config API](https://modrinth.com/mod/cloth-config) | Mod | Standard Fabric config library | TODO |
| [YetAnotherConfigLib](https://modrinth.com/mod/yacl) | Mod | Other popular option for Fabric config | TODO |
| [Forge Config API Port](https://modrinth.com/mod/forge-config-api-port) | Mod | Port for forge mods | TODO |

## Performance

These mods are a staple of the Fabric ecosystem and drasticly improves the fps, tps, and load-times of minecraft.

| Name | Type | Description | Confidence |
| - | - | - | - |
| [ImmediatelyFast](https://modrinth.com/mod/immediatelyfast) | Mod | Speed up rendering of various components | TODO |
| [Concurrent Chunk Management Engine](https://modrinth.com/mod/c2me-fabric) | Mod | Better multithreading for chunk generation | TODO |
| [Dynamic FPS](https://modrinth.com/mod/dynamic-fps) | Mod | Gives the GPU a break | TODO |
| [Enhanced Block Entities](https://modrinth.com/mod/ebe) | Mod | Improves rendering of block entities | TODO |
| [Entity Culling](https://modrinth.com/mod/entityculling) | Mod | Doesn't render entities that aren't visable | TODO |
| [FerriteCore](https://modrinth.com/mod/ferrite-core) | Mod | Memory usage optimizations | TODO |
| [Krypton](https://modrinth.com/mod/krypton) | Mod | Network stack optimizations | TODO |
| [LazyDFU](https://modrinth.com/mod/lazydfu) | Mod | Only runs the DataFixerUpper if needed | TODO |
| [Lithium](https://modrinth.com/mod/lithium) | Mod | Massive optimizations to the server execution | TODO |
| [Memory Leak Fix](https://modrinth.com/mod/memoryleakfix) | Mod | Removes memory Leaks | TODO |
| [More Culling](https://modrinth.com/mod/moreculling) | Mod | Doesn't render things that aren't visable | TODO |
| [Sodium](https://modrinth.com/mod/sodium) | Mod | massive overhaul to the rendering engine | TODO |
| [Reese's Sodium Options](https://modrinth.com/mod/reeses-sodium-options) | Mod | More options plus interaction with other mods | TODO |
| [Sodium Extra](https://modrinth.com/mod/sodium-extra) | Mod | More features for Sodium | TODO |
| [Starlight (Fabric)](https://modrinth.com/mod/starlight) | Mod | Decreases time to calculate lighting | TODO |
| [Nvidium](https://modrinth.com/mod/nvidium) | Mod | Takes advantage of Nvidia GPU's architecture | TODO |
| [Indium](https://modrinth.com/mod/indium) | Mod | Fabric rendering API compatability with sodium | TODO |
| [Bobby](https://modrinth.com/mod/bobby) | Mod | Increases rendering distance on servers | TODO |
| [Debugify](https://modrinth.com/mod/debugify) | Mod | Fixes many bugs including some performance bugs | TODO |
| [FastQuit](https://modrinth.com/mod/fastquit) | Mod | Saves worlds in the background | TODO |
| [Clumps](https://modrinth.com/mod/clumps) | Mod | Clumps XP orbs together to reduce lag | TODO |
| [Language Reload](https://modrinth.com/mod/language-reload) | Mod | Reduces language load times | TODO |
| [Chunky](https://modrinth.com/mod/chunky) | Mod | Pre-generate parts of the world | TODO |
| [ThreadTweak](https://modrinth.com/mod/threadtweak) | Mod | Smooths out some threading issues | TODO |
| [No Unused Chunks](https://modrinth.com/mod/no-unused-chunks) | Mod | Conservativly removes unenhabited chunks when optimizing | TODO |

## Optifine Features

The Optifine client/mod has had a very large impact on the minecraft modding community. Optifine includes a host of features that are quiticential to the look and feel of the game.

### Features

| Name | Type | Description | Confidence |
| - | - | - | - |
| [Puzzle](https://modrinth.com/mod/puzzle) | Mod | Config and other features of Optifine | TODO |
| [Iris](https://modrinth.com/mod/iris) | Mod | Shader support | TODO |
| [Continuity](https://modrinth.com/mod/continuity) | Mod | Connected textures | TODO |
| [LambDynamicLights](https://modrinth.com/mod/lambdynamiclights) | Mod | Adds dynamic lights | TODO |
| [LambdaBetterGrass](https://modrinth.com/mod/lambdabettergrass) | Mod | Better grass and snow | TODO |
| [CITResewn](https://modrinth.com/mod/cit-resewn) | Mod | Custom item textures | TODO |
| [Entity Model Features](https://modrinth.com/mod/entity-model-features) | Mod | Custom entity models | TODO |
| [Entity Texture Features](https://modrinth.com/mod/entitytexturefeatures) | Mod | Custom entity textures | TODO |
| [Borderless Mining](https://modrinth.com/mod/borderless-mining) | Mod | Borderless window instead of Fullscreen | TODO |
| [Zoomify](https://modrinth.com/mod/zoomify) | Mod | Allows zooming in | TODO |
| [Fabrishot](https://modrinth.com/mod/fabrishot) | Mod | 4k Screenshots | TODO |

### Related Shaders and Resource Packs

| Name | Type | Description | Confidence |
| - | - | - | - |
| [BetterVanillaBuilding Overlays](https://modrinth.com/resourcepack/bettervanillabuildingoverlays) | Resource Pack | Complete overhaul of most textures | TODO |
| [BetterVanillaBuilding](https://modrinth.com/resourcepack/bettervanillabuilding) | Resource Pack | Adds connected textures | TODO |
| [BSL Shaders](https://modrinth.com/shader/bsl-shaders) | Shader | Most common shader | TODO |
| [Complementary Shaders - Reimagined](https://modrinth.com/shader/complementary-reimagined) | Shader | Overall well balenced shader | TODO |
| [Rethinking Voxels](https://modrinth.com/shader/rethinking-voxels) | Shader | Ray tracing feel without ray tracing | TODO |
| [Fresh Animations](https://modrinth.com/resourcepack/fresh-animations) | Resource Pack | Animations like minecraft promo videos | TODO |
| [BetterVanillaBuilding x Fresh Animations](https://modrinth.com/resourcepack/bettervanillabuilding-x-freshanimations) | Resource Pack | Compatability with Fresh Animations | TODO |
| [Eating Animation - BetterVanillaBuilding Addon](https://modrinth.com/resourcepack/bvb-eating-animation) | Resource Pack | Compatability with Eating Animation | TODO |
| [Dark GUI - BetterVanillaBuilding addon](https://modrinth.com/resourcepack/dark-gui) | Resource Pack | Dark mode for BVB | TODO |

## Player Interaction, Movement and View

As with any other game, how the player is implemented contributes a lot to the game. Vanilla minecraft shows the first person view as a 2D hand; this can be improved. Many additional features can be added to give a better sense of realism.

Additionally how the player feels when they move and look around the world is just as important. Limiting some features like sitting to only a couple corners of the game limits the freedom of the player.

### Player

| Name | Type | Description | Confidence |
| - | - | - | - |
| [First-person Model](https://modrinth.com/mod/first-person-model) | Mod | Visable hands and legs | TODO |
| [Not Enough Animations](https://modrinth.com/mod/not-enough-animations) | Mod | Better player animations | TODO |
| [3D Skin Layers](https://modrinth.com/mod/3dskinlayers) | Mod | Second layer of players skins are now 3D | TODO |
| [Show Me Your Skin!](https://modrinth.com/mod/show-me-your-skin) | Mod | Configuable option to make player armor invisable | TODO |
| [Eating Animation](https://modrinth.com/mod/eating-animation) | Mod | Food is eated piece by piece | TODO |
| [Model Gap Fix](https://modrinth.com/mod/modelfix) | Mod | Fixes the bugged lines in held items | TODO |

### Movement

| Name | Type | Description | Confidence |
| - | - | - | - |
| [Sit](https://modrinth.com/mod/bl4cks-sit) | Mod | Allows the player to sit on slabs and chairs | TODO |
| [Crawl](https://modrinth.com/mod/crawl) | Mod | Allows the player to crawl at any time | TODO |

### View

| Name                                                                  | Type | Description                         | Confidence |
| --------------------------------------------------------------------- | ---- | ----------------------------------- | ---------- |
| [Freecam](https://modrinth.com/mod/freecam)                           | Mod  | Creative like camera in survival    | TODO       |
| [Freelook](https://modrinth.com/mod/freelook)                         | Mod  | Turn your head like an owl          | TODO       |
| [Better Third Person](https://modrinth.com/mod/better-third-person)   | Mod  | Makes 3rd person intuitive          | TODO       |

## World Generation, Skybox, and water

The player is always interacting with the environment around them. Minecraft's default world generation has improved with time but can look and feel better. Whether it be better looking moutains and oceans, or more adventurous structures, the player will feel more immersed in their world.

### Overworld
| Name                                                                                      | Type          | Description                                   | Confidence |
| ----------------------------------------------------------------------------------------- | ------------- | --------------------------------------------- | ---------- |
| [Tectonic](https://modrinth.com/datapack/tectonic/versions)                               | Datapack/Mod  | Overhauls the overworld biome formation       | TODO       |
| [William Wythers' Overhauled Overworld](https://modrinth.com/mod/wwoo)                    | Mod           | Overhauls the overworld biome look and feel   | TODO       |
| [Towns and Towers](https://modrinth.com/mod/towns-and-towers)                             | Datapack/Mod  | Adds new villages and pillager structures     | TODO       |
| [Custom Stars](https://www.curseforge.com/minecraft/mc-mods/custom-stars)                 | Mod           | Reworks the stars at night                    | TODO       |
| [Better Clouds](https://modrinth.com/mod/better-clouds)                                   | Mod           | Reworks the clouds                            | TODO       |
| [Cubic Sun & Moon](https://modrinth.com/resourcepack/cubic-sun-moon)                      | Resource Pack | Makes the sun and moon into cubes             | TODO       |
| [YUNG's Better Desert Temples](https://modrinth.com/mod/yungs-better-desert-temples)      | Mod           | Desert temples have puzzles and a boss        | TODO       |
| [YUNG's Better Dungeons](https://modrinth.com/mod/yungs-better-dungeons)                  | Mod           | Not boring dungeons                           | TODO       |
| [YUNG's Better Jungle Temples](https://modrinth.com/mod/yungs-better-jungle-temples)      | Mod           | Not boring jungle temples                     | TODO       |
| [YUNG's Better Mineshafts](https://modrinth.com/mod/yungs-better-mineshafts)              | Mod           | Mineshaft overhaul                            | TODO       |
| [YUNG's Better Ocean Monuments](https://modrinth.com/mod/yungs-better-ocean-monuments)    | Mod           | Larger monuments and includes a trident       | TODO       |
| [YUNG's Better Strongholds](https://modrinth.com/mod/yungs-better-strongholds)            | Mod           | Stronghold overhaul                           | TODO       |
| [YUNG's Better Witch Huts](https://modrinth.com/mod/yungs-better-witch-huts)              | Mod           | Witch hut overhaul                            | TODO       |
| [YUNG's Extras](https://modrinth.com/mod/yungs-extras)                                    | Mod           | Adds small ruins and such                     | TODO       |
| [Snow Under Trees](https://modrinth.com/mod/snow-under-trees-remastered)                  | Mod           | Makes snow generate under trees               | TODO       |
| [BedrockWaters](https://modrinth.com/mod/bedrockwaters)                                   | Mod           | Makes water foggier                           | TODO       |
| [Simple Fog Control](https://modrinth.com/mod/simplefog)                                  | Mod           | Better fog controls                           | TODO       |
| [No World Border](https://modrinth.com/resourcepack/invisible-world-border)               | Resource Pack | The world border gets distracting             | TODO       |

### Nether
| Name | Type | Description | Confidence |
| - | - | - | - |
| [Amplified Nether](https://modrinth.com/mod/amplified-nether) | Mod | Taller nether and 3D biomes | TODO |
| [YUNG's Better Nether Fortresses](https://modrinth.com/mod/yungs-better-nether-fortresses) | Mod | More detailed fortresses with a central keep | TODO |

### End
| Name                                                                          | Type          | Description                       | Confidence |
| ----------------------------------------------------------------------------- | ------------- | --------------------------------- | ---------- |
| [Nullscape](https://modrinth.com/mod/nullscape)                               | Datapack/Mod  | Not boring end generation         | TODO       |
| [YUNG's Better End Island](https://modrinth.com/mod/yungs-better-end-island)  | Mod           | End island structures overhaul    | TODO       |
| [Better End Sky](https://modrinth.com/mod/better-end-sky)                     | Mod           | End sky is no longer boring       | TODO       |

## Sound

As the player interacts with the world, they will both see and hear the environment. To better immerse the player in the world around them, a sound overhaul is needed.

| Name                                                                          | Type | Description                            | Confidence |
| ----------------------------------------------------------------------------- | ---- | -------------------------------------- | ---------- |
| [AmbientSounds](https://modrinth.com/mod/ambientsounds)                       | Mod  | Adds chirping bird sounds and more     | TODO       |
| [Presence Footsteps](https://modrinth.com/mod/presence-footsteps)             | Mod  | Footsteps make reasonable sounds       | TODO       |
| [Sound Physics Remastered](https://modrinth.com/mod/sound-physics-remastered) | Mod  | Reverb and more from the environment   | TODO       |

## HUD

The player's HUD is how the game conveys important information. While vanilla minecraft does a good job at this, the HUD is not required all the time. Additionally some extra features can be added.

| Name                                                                                                                  | Type          | Description                                       | Confidence |
| --------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------- | ---------- |
| [Auto HUD](https://modrinth.com/mod/autohud)                                                                          | Mod           | Hides the HUD when not needed                     | 10/10      |
| [Dynamic Crosshair](https://modrinth.com/mod/dynamiccrosshair)                                                        | Mod           | Conveys information based on possible actions     | 10/10      |
| [WTHIT](https://modrinth.com/mod/wthit)                                                                               | Mod           | Shows extra information about the block in view   | TODO       |
| [Detail Armor Bar](https://modrinth.com/mod/detail-armor-bar)                                                         | Mod           | The armor bar displayes the type of armor worn    | TODO       |
| [AppleSkin](https://modrinth.com/mod/appleskin)                                                                       | Mod           | More information about what you're eating         | TODO       |
| [Better Ping Display](https://modrinth.com/mod/better-ping-display-fabric)                                            | Mod           | Shows actual ping value instead of bars           | TODO       |
| [BetterF3](https://modrinth.com/mod/betterf3)                                                                         | Mod           | Makes the F3 screen more readable                 | TODO       |
| [Advancement Plaques](https://modrinth.com/mod/advancement-plaques)                                                   | Mod           | Makes advancements feel like an acomplishment     | TODO       |
| [Embellished Stone (Advancements Plaques)](https://modrinth.com/resourcepack/embellished-stone-advancements-plaques)  | Resource Pack | Reskin for Advancement Plaques                    | TODO       |
| [Beautified Chat](https://modrinth.com/mod/beautified-chat-client)                                                    | Mod           | Reformats chat to have a timestamp                | TODO       |
| [Enhanced Boss Bars](https://modrinth.com/resourcepack/enhanced-boss-bars)                                            | Resource Pack | No longer just a bar                              | TODO       |
| [Highlight](https://modrinth.com/mod/highlight)                                                                       | Mod           | outline selected blocks properly                  | TODO       |
| [More Chat History](https://modrinth.com/mod/morechathistory)                                                         | Mod           | Chat from a week ago                              | TODO       |
| [Status Effect Bars](https://modrinth.com/mod/status-effect-bars)                                                     | Mod           | Better display for status effects                 | TODO       |

## Menu

Menus are how users interact with any non-immediate information. Whether this is a players inventory, crafting table, mod config screen, or changing render settings, menues are how players interact with more complex parts of the game.

| Name                                                                                  | Type          | Description                               | Confidence |
| ------------------------------------------------------------------------------------- | ------------- | ----------------------------------------- | ---------- |
| [Blur](https://modrinth.com/mod/blur-fabric)                                          | Mod           | Blurs the background when in a menu       | 10/10      |
| [InvMove](https://modrinth.com/mod/invmove)                                           | Mod           | Allows movement while in a menu           | TODO       |
| [Portal GUI](https://modrinth.com/mod/portalgui)                                      | Mod           | You can now open a menu in a portal       | TODO       |
| [Smooth Swapping](https://modrinth.com/mod/smooth-swapping)                           | Mod           | Items no longer teleport                  | TODO       |
| [Shulker Box Tooltip](https://modrinth.com/mod/shulkerboxtooltip)                     | Mod           | View the contents of a shulker box        | TODO       |
| [Better Statistics Screen](https://modrinth.com/mod/better-stats)                     | Mod           | Better interface for statistics           | TODO       |
| [Better Recipe Book](https://modrinth.com/mod/brb)                                    | Mod           | Recipe book for more crafting blocks      | TODO       |
| [Cherished Worlds](https://modrinth.com/mod/cherished-worlds)                         | Mod           | Favorite world to protect them            | TODO       |
| [Disable Custom Worlds Advice](https://modrinth.com/mod/dcwa)                         | Mod           | I know what I'm doing                     | TODO       |
| [Eclectic Trove](https://modrinth.com/resourcepack/eclectic-trove-legendary-tooltips) | Resource Pack | Reskin for Legendary Tooltips             | TODO       |
| [Legendary Tooltips](https://modrinth.com/mod/legendary-tooltips)                     | Mod           | Legendary items have legendary borders    | TODO       |
| [Remove Reloading Screen](https://modrinth.com/mod/rrls)                              | Mod           | Reloading occurs in the background        | TODO       |

## Particles

Particles can be used to add more movement and activity to a world. Minecraft's particle system is strong but computationally ineffecient; until a particle performance mod arives, the amount should be limited.

| Name                                                          | Type | Description                                     | Confidence |
| ------------------------------------------------------------- | ---- | ----------------------------------------------- | ---------- |
| [Cave Dust](https://modrinth.com/mod/cave-dust)               | Mod  | Adds grey dust particles underground            | TODO       |
| [Effective](https://modrinth.com/mod/effective)               | Mod  | Adds multiple effects plus water splashes       | TODO       |
| [Falling Leaves](https://modrinth.com/mod/fallingleaves)      | Mod  | Leaf blocks drop leaves                         | TODO       |
| [Make Bubbles Pop](https://modrinth.com/mod/make_bubbles_pop) | Mod  | Bubbles pop realistically                       | TODO       |
| [Visuality](https://modrinth.com/mod/visuality)               | Mod  | Particles for mobs and environments             | TODO       |
| [Wakes](https://modrinth.com/mod/wakes)                       | Mod  | No particles but similar effect to Effective    | TODO       |

## Vanilla+

As minecraft has been developed over the years, some features have either been overlooked or forgoten. Multiple mods have come to fill in the gaps of the game by changing how minecraft plays while still in a vanilla style.

### Client
| Name                                                      | Type | Description                                 | Confidence |
| --------------------------------------------------------- | ---- | ------------------------------------------- | ---------- |
| [AutoTools](https://modrinth.com/mod/minecraft_autotools) | Mod  | Saves time by automatically switching tools | 10/10      |
| [JJElytraSwap](https://modrinth.com/mod/jjelytraswap)     | Mod  | Swap elytra when trying to fly              | 10/10      |
| [Realistic Bees](https://modrinth.com/mod/realistic-bees) | Mod  | Bees are smaller                            | TODO       |
| [SwingThrough](https://modrinth.com/mod/swingthrough)     | Mod  | Don't let grass get in the way              | 10/10      |

### Server
| Name                                                                              | Type      | Description                                       | Confidence |
| --------------------------------------------------------------------------------- | --------- | ------------------------------------------------- | ---------- |
| [track raw statistics](https://vanillatweaks.net/picker/datapacks/)               | Datapack  | Keep track of more player activities              | TODO       |
| [wandering trades](https://vanillatweaks.net/picker/datapacks/)                   | Datapack  | Wandering traders now sell block heads            | TODO       |
| [Better Ladders](https://modrinth.com/mod/better-ladders)                         | Mod       | Ladders can now hang                              | TODO       |
| [Better Totem of Undying](https://modrinth.com/mod/better-totem-of-undying-forge) | Mod       | A totem of undying will always save you           | TODO       |
| [Bottle Your Xp](https://modrinth.com/mod/bottle-your-xp)                         | Mod       | Crouch with a bottle to extract your xp           | TODO       |
| [Bottled Air](https://modrinth.com/mod/bottled-air)                               | Mod       | Empty bottles can be used for air                 | TODO       |
| [ChickensShed](https://modrinth.com/mod/chickensshed)                             | Mod       | Chickens drop feathers                            | TODO       |
| [Configurable Despawn Timer](https://modrinth.com/mod/configurable-despawn-timer) | Mod       | items no longer vanish after 5 minutes            | TODO       |
| [Crying Portals](https://modrinth.com/mod/crying-portals)                         | Mod       | Crying obsidian also works for portals            | TODO       |
| [Double Doors](https://modrinth.com/mod/double-doors)                             | Mod       | Open both doors at the same time                  | TODO       |
| [Grabby Mobs](https://modrinth.com/mod/grabby-mobs)                               | Mod       | Mobs will always grab items if capable            | TODO       |
| [ItemPhysic](https://modrinth.com/mod/itemphysic)                                 | Mod       | Items look like block and sink/float realisticly  | TODO       |
| [Just Mob Heads](https://modrinth.com/mod/just-mob-heads)                         | Mod       | Mobs drop their head                              | TODO       |
| [Keep My Soil Tilled](https://modrinth.com/mod/keep-my-soil-tilled)               | Mod       | Pumpkins don't ruin the tilled soil               | TODO       |
| [Milk All The Mobs](https://modrinth.com/mod/milk-all-the-mobs)                   | Mod       | Why no goat milk? Now you can                     | TODO       |
| [No Feather Trample](https://modrinth.com/mod/no-feather-trample)                 | Mod       | Farmland isn't trampled if wearing featherfalling | TODO       |
| [Nutritious Milk](https://modrinth.com/mod/nutritious-milk)                       | Mod       | Milk acts like a food                             | TODO       |
| [Nyf's Spiders](https://modrinth.com/mod/nyfs-spiders)                            | Mod       | Spiders act like spiders                          | TODO       |
| [Overworld Piglins](https://modrinth.com/mod/overworld-piglins)                   | Mod       | Piglins can resist the overworld                  | TODO       |
| [Passive Endermen](https://modrinth.com/mod/passive-endermen)                     | Mod       | Endermen no longer place blocks                   | TODO       |
| [Quick Right-Click](https://modrinth.com/mod/quick-right-click)                   | Mod       | You don't need to always place crafting blocks    | TODO       |
| [Replanting Crops](https://modrinth.com/mod/replanting-crops)                     | Mod       | Replant with a hoe                                | TODO       |
| [Shulker Drops Two](https://modrinth.com/mod/shulker-drops-two)                   | Mod       | Shulkers drop both their shells                   | TODO       |
| [Skeleton Horse Spawn](https://modrinth.com/mod/skeleton-horse-spawn)             | Mod       | Skeleton horses spawn naturally                   | TODO       |
| [Smaller Nether Portals](https://modrinth.com/mod/smaller-nether-portals)         | Mod       | Nether portals can be any size                    | TODO       |
| [Smelting Plus](https://modrinth.com/mod/smelting-plus)                           | Mod       | Melting tools and armor gives more                | TODO       |
| [Solid Mobs](https://modrinth.com/mod/solid_mobs)                                 | Mod       | You can't walk through a cow                      | TODO       |
| [Spawn Animations](https://modrinth.com/mod/spawn-animations)                     | Mod       | Mobs no longer poof into existance                | TODO       |
| [Stackables](https://modrinth.com/mod/stackables)                                 | Mod       | lets more items stack                             | TODO       |
| [Thorny Bush Protection](https://modrinth.com/mod/thorny-bush-protection)         | Mod       | Don't get pricked if you have pants               | TODO       |
| [Time & Wind](https://modrinth.com/mod/time-wind)                                 | Mod       | Longer or shorter days                            | TODO       |
| [Universal Bone Meal](https://modrinth.com/mod/universal-bone-meal)               | Mod       | Sugar cane is a plant too                         | TODO       |
| [Village Spawn Point](https://modrinth.com/mod/village-spawn-point)               | Mod       | Start in a village                                | TODO       |
| [Villager Names](https://modrinth.com/mod/villager-names-serilum)                 | Mod       | Villagers spawn with names                        | TODO       |
| [Zombie Horse Spawn](https://modrinth.com/mod/zombie-horse-spawn)                 | Mod       | Zombie horses spawn naturally                     | TODO       |


### Recipes

| Name                                                                  | Type | Description                             | Confidence |
| --------------------------------------------------------------------- | ---- | --------------------------------------- | ---------- |
| [Chain Armor Recipe](https://modrinth.com/mod/chain-armor-recipe)     | Mod  | Make chain armor with chain             | TODO       |
| [Craft Saddles](https://modrinth.com/mod/craftsaddles)                | Mod  | Make saddles with leather and such      | TODO       |
| [Name Tag Tweaks](https://modrinth.com/mod/name-tag-tweaks)           | Mod  | Adds a recipe for name tags             | TODO       |
| [Obtainable End](https://modrinth.com/mod/obtainable-end)             | Mod  | End portals shouldn't be unobtainable   | TODO       |
| [Village Bell Recipe](https://modrinth.com/mod/village-bell-recipe)   | Mod  | Adds a recipe for bells                 | TODO       |
| [Wool Tweaks](https://modrinth.com/mod/wool-tweaks)                   | Mod  | Recipe for string plus more features    | TODO       |

# External Tools

## Overview

Sometimes Things are better done with external applications; specifically, optimizing worlds and debugging.

| Name                                                      | Description               |
| --------------------------------------------------------- | ------------------------- |
| [MCA Selector](https://github.com/Querz/mcaselector)      | Delete or generate chunks |
| [NBTExplorer](https://github.com/jaquadro/NBTExplorer)    | Debug NBT information     |
| [World Painter](https://www.worldpainter.net/)            | Make your custom worlds   |
