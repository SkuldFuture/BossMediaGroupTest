from drf_spectacular.utils import extend_schema, extend_schema_view


tasks_scheme = extend_schema_view(
    create=extend_schema(
        summary="Создание задачи",
        description="Создает новую задачу в системе. Возвращает созданную задачу.",
    ),
    retrieve=extend_schema(
        summary="Получение задачи",
        description="Возвращает задачу по ее ID.",
    ),
    list=extend_schema(
        summary="Получение списка задач",
        description="Возвращает список всех задач в системе.",
    ),
    update=extend_schema(
        summary="Обновление задачи",
        description="Обновляет существующую задачу по ее ID. Возвращает обновленную задачу.",
    ),
    partial_update=extend_schema(
        summary="Частичное обновление задачи",
        description="Обновляет одну или несколько полей задачи по ее ID. Возвращает обновленную задачу.",
    ),
    destroy=extend_schema(
        summary="Удаление задачи",
        description="Удаляет существующую задачу по ее ID. Возвращает код 204 при успешном удалении задачи.",
    )
)
