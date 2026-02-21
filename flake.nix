{
  description = "EZroot build environment";

  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system};
      scripts = import ./scripts.nix {inherit pkgs;};
    in {
      devShells.default = pkgs.mkShell {
        buildInputs = with pkgs; [android-tools python3 python313Packages.textual];

        inputsFrom = [];

        shellHook = ''
          alias run="python3 main.py"
          alias exit="adb kill-server && exit"
          adb start-server &> /dev/null
          echo
          onefetch
          echo
          echo "EZroot build environment now running!"
        '';
      };
    });
}
