from abc import ABC, abstractmethod
from typing import Optional, List

from phi.agent.session import AgentSession


class AgentStorage(ABC):
    @abstractmethod
    def create(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def read(self, session_id: str) -> Optional[AgentSession]:
        raise NotImplementedError

    @abstractmethod
    def get_all_session_ids(self, user_id: Optional[str] = None) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def get_all_sessions(self, user_id: Optional[str] = None) -> List[AgentSession]:
        raise NotImplementedError

    @abstractmethod
    def upsert(self, session: AgentSession) -> Optional[AgentSession]:
        raise NotImplementedError

    @abstractmethod
    def delete(self) -> None:
        raise NotImplementedError
