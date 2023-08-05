#!../venv/bin/pytest -s

from confattr import NotificationLevel, UiNotifier


# ------- NotificationLevel -------

def test__notification_level__compare_different() -> None:
	assert NotificationLevel.ERROR > NotificationLevel.INFO
	assert NotificationLevel.ERROR >= NotificationLevel.INFO
	assert NotificationLevel.ERROR != NotificationLevel.INFO  # type: ignore [comparison-overlap]

	assert not NotificationLevel.ERROR < NotificationLevel.INFO
	assert not NotificationLevel.ERROR <= NotificationLevel.INFO
	assert not NotificationLevel.ERROR == NotificationLevel.INFO  # type: ignore [comparison-overlap]
	assert not NotificationLevel.ERROR is NotificationLevel.INFO  # type: ignore [comparison-overlap]

def test__notification_level__compare_same() -> None:
	assert not NotificationLevel.INFO > NotificationLevel.INFO
	assert not NotificationLevel.INFO < NotificationLevel.INFO
	assert not NotificationLevel.INFO != NotificationLevel.INFO

	assert NotificationLevel.INFO <= NotificationLevel.INFO
	assert NotificationLevel.INFO >= NotificationLevel.INFO
	assert NotificationLevel.INFO == NotificationLevel.INFO
	assert NotificationLevel.INFO is NotificationLevel.INFO


# ------- UiNotifier -------

class MockUI:

	def __init__(self) -> None:
		self.messages: 'list[tuple[NotificationLevel, str|BaseException]]' = []

	def reset(self) -> None:
		self.messages.clear()

	def show(self, lvl: NotificationLevel, msg: 'str|BaseException') -> None:
		self.messages.append((lvl, msg))


def test__ui_notifier__notification_level_info() -> None:
	ui_notifier = UiNotifier(notification_level=NotificationLevel.INFO)
	ui = MockUI()
	ui_notifier.set_ui_callback(ui.show)

	ui.reset()
	ui_notifier.show_error('boom')
	assert ui.messages == [(NotificationLevel.ERROR, 'boom')]

	ui.reset()
	ui_notifier.show_info('fyi')
	assert ui.messages == [(NotificationLevel.INFO, 'fyi')]

def test__ui_notifier__notification_level_error() -> None:
	ui_notifier = UiNotifier(notification_level=NotificationLevel.ERROR)
	ui = MockUI()
	ui_notifier.set_ui_callback(ui.show)

	ui.reset()
	ui_notifier.show_error('boom')
	assert ui.messages == [(NotificationLevel.ERROR, 'boom')]

	ui.reset()
	ui_notifier.show_info('fyi')
	assert ui.messages == []


def test__ui_notifier__store_messages() -> None:
	ui_notifier = UiNotifier()

	ui_notifier.show_info('info 1')
	ui_notifier.show_error('error 1')
	ui_notifier.notification_level = NotificationLevel.INFO
	ui_notifier.show_error('error 2')
	ui_notifier.show_info('info 2')

	ui = MockUI()
	ui_notifier.set_ui_callback(ui.show)
	assert ui.messages == [
		(NotificationLevel.ERROR, 'error 1'),
		(NotificationLevel.ERROR, 'error 2'),
		(NotificationLevel.INFO, 'info 2'),
	]
