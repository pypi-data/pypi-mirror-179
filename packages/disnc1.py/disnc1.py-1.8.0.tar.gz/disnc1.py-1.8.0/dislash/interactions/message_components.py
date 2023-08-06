from __future__ import annotations
import re
from abc import ABC, abstractmethod
from typing import cast, Iterable, List, Optional, Union

import discord
from discord import PartialEmoji

from .types import ActionRowPayload, ComponentPayload, SelectMenuPayload, SelectOptionPayload, ButtonStyle, ButtonPayload, ComponentType

__all__ = (
    "auto_rows",
    "ComponentType",
    "ButtonStyle",
    "Component",
    "Button",
    "ActionRow",
    "SelectOption",
    "MenuOption",
    "SelectMenu",
    "_component_factory",
)


ID_SOURCE = 0
MAX_ID = 25


def _partial_emoji_converter(argument: str) -> discord.PartialEmoji:
    if len(argument) < 5:
        # Sometimes unicode emojis are actually more than 1 symbol
        return discord.PartialEmoji(name=argument)

    match = re.match(r"<(a?):([a-zA-Z0-9\_]+):([0-9]+)>$", argument)
    if match is not None:
        emoji_animated = bool(match.group(1))
        emoji_name = match.group(2)
        emoji_id = int(match.group(3))

        return discord.PartialEmoji(name=emoji_name, animated=emoji_animated, id=emoji_id)

    raise discord.InvalidArgument(f"Failed to convert {argument} to PartialEmoji")


def _component_factory(data: ComponentPayload) -> Component:
    _type = data.get("type")
    if _type == 1:
        data = cast(ActionRowPayload, data)
        return ActionRow.from_dict(data)
    elif _type == 2:
        data = cast(ButtonPayload, data)
        return Button.from_dict(data)
    elif _type == 3:
        data = cast(SelectMenuPayload, data)
        return SelectMenu.from_dict(data)
    raise ValueError("Invalid component type")


def auto_rows(*buttons: Button, max_in_row: int = 5) -> List[ActionRow]:
    """
    Distributes buttons across multiple rows
    and returns the list of rows.
    Example
    -------
    ::

        rows = auto_rows(
            Button(label="Red", custom_id="red", style=4),
            Button(label="Green", custom_id="green", style=3),
            max_in_row=1
        )
        await ctx.send("Buttons", components=rows)

    Parameters
    ----------
    buttons : List[:class:`Button`]
        a list of buttons to distribute
    max_in_row : :class:`int`
        limit of buttons in a single row. Must be between 1 and 5.

    Returns
    -------
    List[:class:`ActionRow`]
        the list of rows with buttons
    """
    if not (1 <= max_in_row <= 5):
        raise discord.InvalidArgument("max_in_row parameter should be between 1 and 5.")
    return [
        ActionRow(*buttons[i : i + max_in_row]) for i
        in range(0, len(buttons), max_in_row)
    ]


class SelectOption:
    """
    This class represents an option in a select menu.

    Parameters
    ----------
    label : :class:`str`
        the user-facing name of the option, max 25 characters
    value : :class:`str`
        the dev-define value of the option, max 100 characters
    description : :class:`str`
        an additional description of the option, max 50 characters
    emoji : :class:`str`
        will add an emoji to the option
    default : :class:`bool`
        will render this option as selected by default
    """

    __slots__ = ("label", "value", "description", "emoji", "default")

    label: str
    value: str
    description: str
    emoji: PartialEmoji
    default: bool

    def __init__(
        self,
        label: str,
        value: str,
        description: Optional[str] = None,
        emoji: Optional[Union[str, PartialEmoji]] = None,
        default: bool = False,
    ) -> None:
        if isinstance(emoji, str):
            emoji = _partial_emoji_converter(emoji)

        self.label = label
        self.value = value
        self.description = description
        self.emoji = emoji
        self.default = default

    def __repr__(self) -> str:
        return (
            "<OptionSelect label={0.label!r} value={0.value!r} "
            "description={0.description!r} emoji={0.emoji!r} default={0.default!r}>"
        ).format(self)

    @classmethod
    def from_dict(cls, data: SelectOptionPayload) -> SelectOption:
        emoji = data.get("emoji")
        if emoji is not None:
            emoji = discord.PartialEmoji.from_dict(emoji)
        return cls(
            label=data["label"],
            value=data["value"],
            description=data.get("description"),
            emoji=emoji,
            default=data.get("default", False),
        )

    def to_dict(self) -> SelectOptionPayload:
        data = SelectOptionPayload(label=self.label, value=self.value)
        if self.description is not None:
            data["description"] = self.description
        if self.emoji is not None:
            data["emoji"] = self.emoji.to_dict()
        if self.default:
            data["default"] = self.default
        return data


class Component(ABC):
    """
    The base class for message components
    """

    disabled: bool
    custom_id: Optional[str]
    type: int

    def __init__(self, type: int) -> None:
        self.type = type

    @abstractmethod
    def to_dict(self) -> ComponentPayload:
        raise NotImplementedError


class SelectMenu(Component):
    """
    This class represents a select menu.

    Parameters
    ----------
    custom_id : :class:`str`
        a developer-defined identifier for the button, max 100 characters
    placeholder : :class:`str`
        custom placeholder text if nothing is selected, max 100 characters
    min_values : :class:`int`
        the minimum number of items that must be chosen; default 1, min 0, max 25
    max_values : :class:`int`
        the maximum number of items that can be chosen; default 1, max 25
    options : List[:class:`SelectOption`]
        the choices in the select, max 25
    disabled : :class:`bool`
        disable the menu, defaults to false

    Attributes
    ----------
    custom_id : :class:`str`
        a developer-defined identifier for the button, max 100 characters
    placeholder : :class:`str`
        custom placeholder text if nothing is selected, max 100 characters
    min_values : :class:`int`
        the minimum number of items that must be chosen; default 1, min 0, max 25
    max_values : :class:`int`
        the maximum number of items that can be chosen; default 1, max 25
    options : List[:class:`SelectOption`]
        the choices in the select, max 25
    disabled : :class:`bool`
        disable the menu, defaults to false
    selected_options : List[:class:`SelectOption`]
        the list of chosen options, max 25
    """

    placeholder: Optional[str] = None
    min_values: int = 1
    max_values: int = 1
    options: List[SelectOption]
    disabled: bool = False

    def __init__(
        self,
        *,
        custom_id: Optional[str] = None,
        placeholder: Optional[str] = None,
        min_values: int = 1,
        max_values: int = 1,
        options: Optional[List[SelectOption]] = None,
        disabled: bool = False,
    ) -> None:
        super().__init__(3)
        self.custom_id = custom_id or "0"
        self.placeholder = placeholder
        self.min_values = min_values
        self.max_values = max_values
        self.options = options or []
        self.disabled = disabled
        self.selected_options: List[SelectOption] = []

    def __repr__(self) -> str:
        return (
            "<SelectMenu custom_id={0.custom_id!r} placeholder={0.placeholder!r} "
            "min_values={0.min_values!r} max_values={0.max_values!r} options={0.options!r}"
            "disabled={0.disabled} selected_options={0.selected_options!r}>"
        ).format(self)

    def _select_options(self, values: List[str]) -> None:
        self.selected_options = []
        for option in self.options:
            if option.value in values:
                self.selected_options.append(option)

    def add_option(
        self,
        label: str,
        value: str,
        description: Optional[str] = None,
        emoji: Optional[str] = None,
        default: bool = False,
    ) -> None:
        """
        Adds an option to the list of options of the menu.
        Parameters are the same as in :class:`SelectOption`.
        """
        self.options.append(
            SelectOption(
                label=label,
                value=value,
                description=description,
                emoji=emoji,
                default=default
            )
        )

    @classmethod
    def from_dict(cls, data: SelectMenuPayload) -> SelectMenu:
        return cls(
            custom_id=data.get("custom_id"),
            placeholder=data.get("placeholder"),
            min_values=data.get("min_values", 1),
            max_values=data.get("max_values", 1),
            options=[
                SelectOption.from_dict(o) for o
                in data.get("options", [])
            ],
            disabled=data.get("disabled", False),
        )

    def to_dict(self) -> SelectMenuPayload:
        payload = SelectMenuPayload(
            type=self.type,
            custom_id=self.custom_id,
            min_values=self.min_values,
            max_values=self.max_values,
            options=[o.to_dict() for o in self.options],
        )
        if self.placeholder:
            payload["placeholder"] = self.placeholder
        if self.disabled:
            payload["disabled"] = True
        return payload


class Button(Component):
    """
    Builds a button.

    Parameters
    ----------
    style : :class:`ButtonStyle`
        Style of the button
    label : :class:`str`
        Button text
    emoji : :class:`str` | :class:`discord.PartialEmoji`
        Button emoji
    custom_id : :class:`str`
        You should set it by yourself, it's not a snowflake.
        If button style is not :class:`ButtonStyle.link`, this is
        a required field
    url : :class:`str`
        If button style is :class:`ButtonStyle.link`, this is
        a required field.
    disabled : :class:`bool`
        Whether the button is disabled or not. Defaults to false.
    """

    style: ButtonStyle
    label: Optional[str]
    emoji: Optional[discord.PartialEmoji]
    url: Optional[str]

    def __init__(
        self,
        *,
        style: ButtonStyle,
        label: Optional[str] = None,
        emoji: Optional[Union[discord.PartialEmoji, str]] = None,
        custom_id: Optional[str] = None,
        url: Optional[str] = None,
        disabled: bool = False,
    ) -> None:
        global ID_SOURCE  # Ugly as hell

        if custom_id is None:
            if url is None:
                custom_id = str(ID_SOURCE)
                ID_SOURCE = (ID_SOURCE + 1) % MAX_ID
            elif style != ButtonStyle.link:
                raise discord.InvalidArgument("if you specify url, the style must be ButtonStyle.link")
        elif url is not None:
            raise discord.InvalidArgument("you can't specify both url and custom_id")
        elif style == ButtonStyle.link:
            raise discord.InvalidArgument("style 'link' expects url to be specified")

        if isinstance(emoji, str):
            emoji = _partial_emoji_converter(emoji)

        super().__init__(2)
        self.style = style
        self.label = label
        self.emoji = emoji
        self.custom_id = custom_id
        self.url = url
        self.disabled = disabled

    def __repr__(self) -> str:
        return (
            f"<Button custom_id={self.custom_id!r} label={self.label!r} "
            f"style={self.style!r} emoji={self.emoji!r} "
            f"url={self.url!r} disabled={self.disabled!r}>"
        )

    @property
    def id(self) -> Optional[str]:
        return self.custom_id

    @classmethod
    def from_dict(cls, data: ButtonPayload) -> Button:
        emoji = data.get("emoji")
        if emoji is not None:
            emoji = discord.PartialEmoji.from_dict(emoji)
        return cls(
            style=data["style"],
            label=data.get("label"),
            emoji=emoji,
            custom_id=data.get("custom_id"),
            url=data.get("url"),
            disabled=data.get("disabled", False),
        )

    def to_dict(self) -> ButtonPayload:
        payload = ButtonPayload(
            type=self.type,
            style=self.style,
        )
        if self.label is not None:
            payload["label"] = self.label
        if self.emoji is not None:
            payload["emoji"] = self.emoji.to_dict()
        if self.custom_id is not None:
            payload["custom_id"] = self.custom_id
        if self.url is not None:
            payload["url"] = self.url
        if self.disabled:
            payload["disabled"] = self.disabled
        return payload


class ActionRow(Component):
    """
    Represents an action row. Action rows are basically
    shelves for buttons.

    Parameters
    ----------
    components : :class:`List[Button]`
        a list of up to 5 buttons to place in a row
    """

    components: List[Component]

    def __init__(self, *components: Component):
        self._limit = 5
        if len(components) > self._limit:
            raise discord.InvalidArgument(f"components must be a list of up to {self._limit} elements")
        if not all(isinstance(comp, Component) for comp in components):
            raise discord.InvalidArgument("components must be a list of Component")

        super().__init__(1)
        self.components = list(components)

    def __repr__(self) -> str:
        return "<ActionRow components={0.components!r}>".format(self)

    @property
    def buttons(self) -> List[Component]:
        return self.components

    @property
    def _buttons(self) -> Iterable[Button]:
        return (c for c in self.components if isinstance(c, Button))

    @classmethod
    def from_dict(cls, data: ActionRowPayload) -> ActionRow:
        buttons = [_component_factory(elem) for elem in data.get("components", [])]
        return cls(*buttons)

    def to_dict(self) -> ActionRowPayload:
        return ActionRowPayload(
            type=self.type,
            components=[c.to_dict() for c in self.components],
        )

    def disable_buttons(self, *positions: int) -> None:
        """
        Sets ``disabled`` to ``True`` for all buttons in this row.
        """
        if not positions:
            for button in self._buttons:
                button.disabled = True
        else:
            for i in positions:
                component = self.components[i]
                if component.type == ComponentType.Button:
                    component.disabled = True

    def enable_buttons(self, *positions: int) -> None:
        """
        Sets ``disabled`` to ``False`` for all buttons in this row.
        """
        if not positions:
            for button in self._buttons:
                button.disabled = False
        else:
            for i in positions:
                component = self.components[i]
                if component.type == ComponentType.Button:
                    component.disabled = False

    def add_button(
        self,
        *,
        style: ButtonStyle,
        label: Optional[str] = None,
        emoji: Optional[str] = None,
        custom_id: Optional[str] = None,
        url: Optional[str] = None,
        disabled: bool = False,
    ) -> None:
        self.components.append(
            Button(
                style=style,
                label=label,
                emoji=emoji,
                custom_id=custom_id,
                url=url,
                disabled=disabled,
            )
        )

    def add_menu(
        self,
        *,
        custom_id: str,
        placeholder: Optional[str] = None,
        min_values: int = 1,
        max_values: int = 1,
        options: Optional[List[SelectOption]] = None,
    ) -> None:
        self.components.append(
            SelectMenu(
                custom_id=custom_id,
                placeholder=placeholder,
                min_values=min_values,
                max_values=max_values,
                options=options,
            )
        )


MenuOption = SelectOption
