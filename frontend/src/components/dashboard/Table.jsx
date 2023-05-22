import React from 'react';

const Table = ({ props }) => {
    return (
        <table className="table table-hover">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Магазин</th>
                    <th scope="col">Суммарно</th>
                    <th scope="col">Автореги</th>
                    <th scope="col">Аккаунты с БМ</th>
                    <th scope="col">FanPage</th>
                    <th scope="col">Фарм</th>
                    <th scope="col">Остальное</th>
                </tr>
            </thead>
            <tbody>
                {props.map((shop, id) => {
                    return ( 
                        <tr key={'shop_' + id+1}>
                            <th scope="row">{id+1}</th>
                            <td><a href={shop.shop.url} target="_blank" rel="noreferrer" style={{ color: 'black' }}>{new URL(shop.shop.url).hostname}</a></td>
                            <td>{shop.BM_cost + shop.ZRD_cost + shop.Farm_cost + shop.Autoreg_cost + shop.FP_cost + shop.PZRDFP_cost + shop.Undef_cost} ₽</td>
                            <td>{shop.Autoreg_cost} ₽</td>
                            <td>{shop.BM_cost} ₽</td> 
                            <td>{shop.FP_cost} ₽</td>
                            <td>{shop.Farm_cost} ₽</td>
                            <td>{shop.Undef_cost + shop.PZRDFP_cost} ₽</td>
                        </tr>
                    );
                })
                }
            </tbody>
        </table>
    );
};

export default Table;