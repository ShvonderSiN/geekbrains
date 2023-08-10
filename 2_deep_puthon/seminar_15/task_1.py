def divide(a: int | float, b: int | float) -> float | None:
    if b == 0:
        logger.error('На ноль делить нельзя, ZeroDivisionError')
        return None
    return a / b


if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.ERROR,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename='task_1_error.log',
                        filemode='a', encoding='utf-8')
    logger = logging.getLogger(__name__)
    divide(3, 0)
