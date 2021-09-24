# Multiplayer Arena Shooter

The idea behind this project was to create a strong platform for learning and implementing networking in Unreal Engine 5 using c++. 

The result is a third person arena shooter with all main weapon archetypes like sniper, shotgun, full auto weapon etc. 
and features like: scoreboard, inventory(WIP), grenades, ammo/weapon pickups, powerups, complete UI and HUD and some crosshair customization.

This is wraped in 3 main gamemodes: 
- Free For All Deathmatch,
- Team's Deathmatch,
- Capture the flag,
  
and planning on doing CSGO like teams match with bomb.

When it comes to networking this project is utilizing:
- **Client Side Prediction** - for example: updating the hud, reloading, aiming.
- **Server Side Rewind** - for every type of weapon (excluding explosive weapons like Rocket Launcher although projectile predicting is also done with Assault Rifle).
- **Validation** - for ammo changes etc.

- Support environment-specific overrides via separate config files

- Add proper error handling for invalid config so the app doesn't crash on startup

- Handle the duplicate key case by merging the values instead of failing

- Support environment-specific overrides via separate config files

- Bump dependency to get the security fix for the reported CVE

- Update the example config with all available options and comments

- Update the deployment docs with the new environment variables

- Correct the formula used for calculating the backoff delay

- Update the API docs with the new query parameters and examples

- Implement a small in-memory cache for the config to avoid re-reading

- Add a note in the README about the breaking change in 2.0

- Update dependencies and resolve compatibility warning from pytest

- Bump the Docker base image to get the latest security patches

- Implement a small in-memory cache for the config to avoid re-reading

- Bump the version and tag the release in the repo

- Improve error message when the required env var is not set

- Implement basic rate limiting to avoid overwhelming the downstream service

- Remove obsolete workaround now that the upstream bug is fixed
