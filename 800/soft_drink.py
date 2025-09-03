friends, bottles, volume, limes, slices, salt, mm_drink, g_salt = map(
    int, input().split()
)

total_volume = bottles * volume
toasts = total_volume // mm_drink

total_slices = limes * slices

parts_salt = salt // g_salt

ans = min(toasts, total_slices, parts_salt) // friends
print(ans)
