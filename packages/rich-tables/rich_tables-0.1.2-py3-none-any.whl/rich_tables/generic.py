import itertools as it
import json
from functools import partial
from typing import Any, Dict, Iterable, List, Optional, Union

from multimethod import multimethod
from rich import box
from rich.columns import Columns
from rich.console import ConsoleRenderable, RenderableType
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text

from .utils import (
    DISPLAY_HEADER,
    FIELDS_MAP,
    NewTable,
    border_panel,
    counts_table,
    format_with_color,
    make_console,
    make_difftext,
    new_table,
    predictably_random_color,
    simple_panel,
    wrap,
)

JSONDict = Dict[str, Any]
console = make_console()


def mapping_view_table(**kwargs: Any) -> NewTable:
    """A table with two columns
    * First for bold field names
    * Second one for values
    """
    table = new_table(border_style="misty_rose1", box=box.MINIMAL, expand=False)
    table.add_column(justify="right", style="bold misty_rose1")
    table.add_column()
    return table


def prepare_dict(item: JSONDict) -> JSONDict:
    if "before" in item and "after" in item:
        before, after = item.pop("before"), item.pop("after")
        if not item.get("diff"):
            if isinstance(before, list):
                before, after = "\n".join(before), "\n".join(after)

            if isinstance(before, str):
                item["diff"] = make_difftext(before, after)
            else:
                keys = before.keys()
                item["diff"] = json.dumps(
                    {
                        k: make_difftext(str(before[k] or ""), str(after[k] or ""))
                        for k in keys
                    },
                    indent=2,
                )
    return item


@multimethod
def flexitable(data: None, header: str = "") -> RenderableType:
    return str(data)


@flexitable.register
def _(data: str) -> RenderableType:
    if "[/]" not in data:
        data = data.replace("[", "").replace("]", "")
    return " | ".join(map(format_with_color, data.split(" | ")))


@flexitable.register
def _(data: str, header: str) -> RenderableType:
    if "[/]" not in data:
        data = data.replace("[", "").replace("]", "")
    return FIELDS_MAP[header](data)


@flexitable.register
def _(data: Union[int, float], header: Optional[str] = "") -> RenderableType:
    return flexitable(str(data), header)


@flexitable.register
def _(data: JSONDict, header: Optional[str] = "") -> RenderableType:
    data = prepare_dict(data)
    table = mapping_view_table()
    cols = []
    for key, content in data.items():
        if not content:
            continue

        content = flexitable(content, key)
        if isinstance(content, ConsoleRenderable) and not isinstance(content, Markdown):
            cols.append(border_panel(content, title=flexitable(key)))
            # table.add_row(key, border_panel(content))
        else:
            table.add_row(key, content)

    cols.insert(0, table)
    if header:
        return Columns(cols)

    # cols.sort(key=lambda x: console.measure(x).maximum)
    # return new_table(rows=it.zip_longest(*(iter(cols),) * 1))
    table = new_table()
    row, width = [], 0
    rows: List[Panel] = []
    for rend in cols:
        this_width = console.measure(rend).maximum
        if width + this_width > console.width:
            # lines.append(simple_panel(new_table(rows=[row], padding=(0, 0))))
            rows.append(simple_panel(new_table(rows=[row], padding=(0, 0))))
            row, width = [rend], this_width
        else:
            row.append(rend)
            width += this_width
    rows.append(simple_panel(new_table(rows=[row], padding=(0, 0))))
    table.add_rows([[r] for r in rows])
    return table


list_table = partial(new_table, expand=False, box=box.SIMPLE_HEAD, border_style="cyan")


@flexitable.register
def _(data: List[str], header: str = "") -> RenderableType:
    call = FIELDS_MAP.get(header)
    return call("\n".join(data)) if call else "\n".join(map(format_with_color, data))


@flexitable.register
def _(data: List[int], header: Optional[str] = None) -> RenderableType:
    return border_panel(Columns(str(x) for x in data))


@flexitable.register
def _(data: List[JSONDict], header: Optional[str] = None) -> RenderableType:
    data = [prepare_dict(item) for item in data]
    all_keys = dict.fromkeys(it.chain.from_iterable(tuple(d.keys()) for d in data))
    keys = {k: None for k in all_keys if any((d.get(k) for d in data))}.keys()

    if len(keys) > 17:
        table = list_table(show_header=False)
        for item in data:
            table.add_row(flexitable({k: v for k, v in item.items() if k in keys}))
        return table

    overlap = set(map(type, data[0].values())) & {int, float, str}
    keysstr = " ".join(keys)
    counting = any(x in keysstr for x in ["count", "sum_", "duration"])
    if len(overlap) == 2 and counting:
        return counts_table(data, header=header or "")

    table = list_table(show_header=True)
    for key in keys:
        table.add_column(key)
    for item in data:
        table.add_dict_item(item, transform=flexitable)
    for col, old in ((c, str(c.header)) for c in table.columns if c):
        new = DISPLAY_HEADER.get(old) or old
        col.header = wrap(new, f"{predictably_random_color(new)}")

    return table


@flexitable.register
def _(data: List[Any], header: Optional[str] = None) -> ConsoleRenderable:
    table = list_table(show_header=False)
    for item in data:
        content = flexitable(item)
        if isinstance(content, Iterable) and not isinstance(content, str):
            table.add_row(*content)
        else:
            table.add_row(content)

    return simple_panel(table)
