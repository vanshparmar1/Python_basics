def brew_chai(flavour):
    if flavour not in ["masala","ginger","elachi"]:
        raise ValueError("unsupported chai flavour")
    print(f"brewing{flavour} chai")

brew_chai("mint")