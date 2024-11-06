# shell.nix
let
  pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-24.05") {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
      numpy
      pip
    ]))
  ];
}