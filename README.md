# Separator

- **Time Limit**: 1 second
- **Memory Limit**: 256 MB

Hamed and Hamid are brothers.

Hamid loves even numbers because he is "mozdvaj" (even), while Hamed loves odd numbers because he is "monfared" (odd).

Now, these two brothers are given a list of integers, and since each of them is interested in a type of numbers (even or odd), they decide that Hamid will take the even numbers and Hamed will take the odd numbers.

Since these two brothers are busy with other fundamental tasks, they ask you to do this job for them.

Complete the function `separator` so that, given a list of integers, it returns a tuple of two lists in the order they appear in the input list. The first list should contain the even numbers and the second list should contain the odd numbers.

```python
def separator(ls):
    pass
```

### Sample 1

```terminal
>>> separator([-3, -2, -1, 0, 1, 2, 3])
([-2, 0, 2], [-3, -1, 1, 3])
```


### Sample 2

```terminal
>>> separator([1, 11, 5, 7, 3])
([], [1, 11, 5, 7, 3])
```

## Notes

- Your function should not print anything. It should return the desired output.

- The first list returned should contain the even numbers and the second list should contain the odd numbers.

- The numbers in the lists should be in the same order as they appear in the input list.



# مُجَزا

- محدودیت زمان: 1 ثانیه
- محدودیت حافظه: ۲۵۶ مگابایت

حامد و حمید برادر هستند.

از آن‌جایی که حمید، مُزْدَوَجْ است؛ عاشق اعداد زوج و از آن‌جایی که حامد مُنْفَرِد است؛ عاشق اعداد فرد است.

حال به این دو برادر، لیستی از اعداد صحیح داده می‌شود و از آن‌جایی که هر کدام از آن‌ها به یک نوع از اعداد زوج یا فرد علاقه‌مند است؛ تصمیم می‌گیرند که حمید، اعداد زوج و حامد نیز اعداد فرد را برای خود جدا کنند.

از آن‌جایی که این دو برادر درگیر کارهای بنیادین دیگری هستند، از شما می‌خواهند تا این کار را برای آن‌ها انجام دهید.

حال تابع `separator` را به‌گونه‌ای تکمیل کنید که با گرفتن لیستی از اعداد صحیح، تاپلی (tuple) از دو لیست به همان ترتیبی که در لیست ورودی آمده‌اند را بازگرداند که لیست اول شامل اعداد زوج و لیست دوم شامل اعداد فرد باشد.

```python
def separator(ls):
    pass
```

### نمونه ۱

```terminal
>>> separator([-3, -2, -1, 0, 1, 2, 3])
([-2, 0, 2], [-3, -1, 1, 3])
```


### نمونه ۲

```terminal
>>> separator([1, 11, 5, 7, 3])
([], [1, 11, 5, 7, 3])
```

## نکات

- تابع شما نباید مقداری را چاپ کند، بلکه باید مقادیر مورد نظر را بازگرداند.

- لیست بازگردانده‌شده‌ی اول، باید حاوی اعداد زوج و لیست دوم حاوی اعداد فرد باشد. 

- اعداد داخل لیست‌ها، باید به همان ترتیبی که در لیست اولیه قرار داشته‌اند، قرار بگیرند.
