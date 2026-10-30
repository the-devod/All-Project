from enum import Enum, auto
from dataclasses import dataclass
from datetime import datetime, timezone


class AssistantState(Enum):
    IDLE = auto()
    LISTENING = auto()
    PROCESSING = auto()
    SPEAKING = auto()
    ERROR = auto()


@dataclass
class StateTransition:
    previous_state: AssistantState
    current_state: AssistantState
    timestamp: str


class VoiceStateManager:
    """Manages state transitions for the AI Voice Assistant."""

    def __init__(self) -> None:
        self._state: AssistantState = AssistantState.IDLE
        self._history: list[StateTransition] = []

    @property
    def state(self) -> AssistantState:
        return self._state

    def transition_to(self, new_state: AssistantState) -> StateTransition:
        if not isinstance(new_state, AssistantState):
            raise ValueError(f"Invalid state: {new_state}")

        transition = StateTransition(
            previous_state=self._state,
            current_state=new_state,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
        self._state = new_state
        self._history.append(transition)
        return transition

    def reset(self) -> None:
        self.transition_to(AssistantState.IDLE)
