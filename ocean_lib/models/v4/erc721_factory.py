#
# Copyright 2021 Ocean Protocol Foundation
# SPDX-License-Identifier: Apache-2.0
#
from typing import List

from enforce_typing import enforce_types
from ocean_lib.models.v4.erc_token_factory_base import ERCTokenFactoryBase
from ocean_lib.web3_internal.wallet import Wallet


@enforce_types
class ERC721FactoryContract(ERCTokenFactoryBase):
    CONTRACT_NAME = "ERC721Factory"
    EVENT_NFT_CREATED = "NFTCreated"
    EVENT_TOKEN_CREATED = "TokenCreated"
    EVENT_NEW_POOL = "NewPool"
    EVENT_NEW_FIXED_RATE = "NewFixedRate"
    EVENT_DISPENSER_CREATED = "DispenserCreated"

    @property
    def event_NFTCreated(self):
        return self.events.NFTCreated()

    @property
    def event_TokenCreated(self):
        return self.events.TokenCreated()

    @property
    def event_NewPool(self):
        return self.events.NewPool()

    @property
    def event_NewFixedRate(self):
        return self.events.NewFixedRate()

    @property
    def event_DispenserCreated(self):
        return self.events.DispenserCreated()

    def deploy_erc721_contract(
        self,
        name: str,
        symbol: str,
        template_index: int,
        additional_erc20_deployer: str,
        base_uri: str,
        from_wallet: Wallet,
    ):
        return self.send_transaction(
            "deployERC721Contract",
            (name, symbol, template_index, additional_erc20_deployer, base_uri),
            from_wallet,
        )

    def get_current_nft_count(self) -> int:
        return self.contract.caller.getCurrentNFTCount()

    def get_nft_template(self, template_index: int) -> list:
        return self.contract.caller.getNFTTemplate(template_index)

    def get_current_nft_template_count(self) -> int:
        return self.contract.caller.getCurrentNFTTemplateCount()

    def is_contract(self, account_address: str) -> bool:
        return self.contract.caller.isContract(account_address)

    def create_token(
        self,
        template_index: int,
        strings: List[str],
        addresses: List[str],
        uints: List[int],
        bytess: List[bytes],
        from_wallet: Wallet,
    ) -> str:
        return self.send_transaction(
            "createToken",
            (template_index, strings, addresses, uints, bytess),
            from_wallet,
        )

    def get_current_token_count(self) -> int:
        return self.contract.caller.getCurrentTokenCount()

    def get_token_template(self, index: int) -> list:
        return self.contract.caller.getTokenTemplate(index)

    def get_current_template_count(self) -> int:
        return self.contract.caller.getCurrentTemplateCount()

    def template_count(self) -> int:
        return self.contract.caller.templateCount()

    def start_multiple_token_order(
        self,
        token_address: str,
        consumer: str,
        amount: int,
        service_id: int,
        consume_fee_address: str,
        consume_fee_token: str,
        consume_fee_amount: int,
        from_wallet: Wallet,
    ) -> str:
        orders = [
            (
                token_address,
                consumer,
                amount,
                service_id,
                consume_fee_address,
                consume_fee_token,
                consume_fee_amount,
            )
        ]
        return self.send_transaction("startMultipleTokenOrder", (orders,), from_wallet)

    def create_nft_with_erc(
        self,
        nft_create_data: dict,
        erc_create_data: dict,
        from_wallet: Wallet,
    ) -> str:
        return self.send_transaction(
            "createNftWithErc",
            (nft_create_data, erc_create_data),
            from_wallet,
        )

    def create_nft_erc_with_pool(
        self,
        nft_create_data: dict,
        erc_create_data: dict,
        pool_data: dict,
        from_wallet: Wallet,
    ) -> str:
        return self.send_transaction(
            "createNftErcWithPool",
            (nft_create_data, erc_create_data, pool_data),
            from_wallet,
        )

    def create_nft_erc_with_fixed_rate(
        self,
        nft_create_data: dict,
        erc_create_data: dict,
        fixed_data: dict,
        from_wallet: Wallet,
    ) -> str:
        return self.send_transaction(
            "createNftErcWithFixedRate",
            (nft_create_data, erc_create_data, fixed_data),
            from_wallet,
        )

    def create_nft_erc_with_dispenser(
        self,
        nft_create_data: dict,
        erc_create_data: dict,
        dispenser_data: dict,
        from_wallet: Wallet,
    ) -> str:
        return self.send_transaction(
            "createNftErcWithDispenser",
            (nft_create_data, erc_create_data, dispenser_data),
            from_wallet,
        )