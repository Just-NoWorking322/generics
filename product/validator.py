from rest_framework import serializers

BAD_WORDS = ['спам', 'бесплатно', 'реклама', 'лучший', 'самый',
              'хит', '№ 1', 'супер', 'абсолютный', 'идеальный',
              'лечит', 'исцеляет', 'терапия', 'рецепт', 'избавление', 'боли',
              'болезни', 'маты']

def valid_title(value: str):
    val_lower = value.lower()
    for word in BAD_WORDS:
        if word in val_lower:
            raise serializers.ValidationError(
                f'Название не может содержать в себе запрещенные, спам и рекламные слова "{word}"'  
            )
        return value

    