zless ../MCB185/data/dictionary.gz | grep -E "[r]{1,}" | grep -E ".{4,}" | grep -E "[zoncai]{1,}" | grep -v "[bdefghjklmpqstuvwxy]" | wc
