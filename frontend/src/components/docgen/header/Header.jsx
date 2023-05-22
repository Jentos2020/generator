import React from 'react';

const Header = () => {
    return (
        <>
            <h3>
                Monkeygen
                <small className="text-muted ms-2">v1.0</small>
            </h3>
            <p>Итоговое изображение всегда получается уникальным, все элементы немного смещаются в случайном направлении и на случайное количество пикселей, поверх накладываются маски(шум\блики\царапины), фон выбирается случайным образом из имеющейся базы.</p>
        </>
    );
};

export default Header;