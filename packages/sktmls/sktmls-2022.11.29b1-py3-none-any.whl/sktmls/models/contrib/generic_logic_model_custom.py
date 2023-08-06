from typing import Any, Dict, List, Union

import numpy as np
from pandas import DataFrame
from pytz import timezone
import torch

from sktmls import MLSRuntimeENV
from sktmls.apis import MLSProfileAPIClient, MLSGraphAPIClient
from sktmls.dynamodb import DynamoDBClient
from sktmls.models import MLSGenericModel, MLSModelError, MLSTrainableCustom
from sktmls.utils import LogicProcessor

TZ = timezone("Asia/Seoul")

logic_processor = LogicProcessor()


class GenericLogicModelCustom(MLSGenericModel, MLSTrainableCustom):
    """
    MLS 모델 레지스트리에 등록되는 단일 모델 기반의 클래스입니다.
    전처리 로직은 json 형태로 후처리 로직은 별도로 정의한 함수를 전달하여 프로세스합니다.
    """

    def __init__(
        self,
        model_name: str,
        model_version: str,
        features: List[str],
        model=None,
        preprocess_logic: Dict[str, List[Any]] = None,
        postprocess_logic=None,
        predict_fn: str = "predict",
        data: Dict[str, Any] = {},
        user_profile_nm: str = None,
        pf_value: List[str] = None,
    ):
        assert isinstance(features, list), "`features`은 list 타입이어야 합니다."

        if preprocess_logic is not None:
            assert isinstance(preprocess_logic, dict), "`preprocess_logic`은 dict 타입이어야 합니다."
            for key in preprocess_logic.keys():
                assert (
                    key in ["var", "missing", "missing_some", "pf", "with", "for"] or key in logic_processor.operations
                )
        else:
            preprocess_logic = {"merge": [{"var": f} for f in features]}

        if postprocess_logic is not None:
            assert hasattr(postprocess_logic, "__call__") is True, "postprocess_logic 값은 함수이어야 합니다."
        else:
            pass

        assert isinstance(predict_fn, str), "`predict_fn`은 str 타입이어야 합니다."
        assert predict_fn in [
            "predict",
            "predict_proba",
            "none",
        ], "`predict_fn`은 predict, predict_proba, none 중 하나의 값이어야 합니다."

        assert isinstance(data, dict), "`data`는 dict 타입이어야 합니다."

        if user_profile_nm is not None:
            assert isinstance(user_profile_nm, str), "`user_profile_nm`는 str 타입이어야 합니다."
            assert (user_profile_nm is not None) and (
                pf_value is not None
            ), "`user_profile_nm`은 `pf_value`와 함께 입력을 받아야 합니다."
        else:
            user_profile_nm = None

        if pf_value is not None:
            assert isinstance(pf_value, list), "`pf_value`는 list 타입이어야 합니다."
            assert (user_profile_nm is not None) and (
                pf_value is not None
            ), "`user_profile_nm`은 `pf_value`와 함께 입력을 받아야 합니다."
            all_val = [
                "additional_svc_allcare_scrb_type",
                "additional_svc_ansim_option_scrb_type",
                "additional_svc_flo_scrb_type",
                "additional_svc_melon_scrb_type",
                "additional_svc_oksusu_scrb_type",
                "additional_svc_pooq_scrb_type",
                "age",
                "age_band",
                "agrmt_end_bf_d100_yn",
                "agrmt_info_discount_yn",
                "allot_mth_cnt",
                "allot_prn_amt",
                "app_use_cnt_bank",
                "app_use_cnt_etc_video",
                "app_use_cnt_fin_bf_m1",
                "app_use_cnt_flo",
                "app_use_cnt_game",
                "app_use_cnt_melon",
                "app_use_cnt_music",
                "app_use_cnt_shopping",
                "app_use_cnt_video",
                "app_use_cnt_vr",
                "app_use_cnt_youtube",
                "app_use_days_music",
                "app_use_days_music_median_yn",
                "app_use_days_video",
                "app_use_days_video_median_yn",
                "app_use_traffic_11st_bf_m6",
                "app_use_traffic_bank",
                "app_use_traffic_bank_card",
                "app_use_traffic_bugs",
                "app_use_traffic_delivery",
                "app_use_traffic_etc_ai_assistant",
                "app_use_traffic_etc_ai_assistant_median_yn",
                "app_use_traffic_etc_music",
                "app_use_traffic_etc_video",
                "app_use_traffic_facebook",
                "app_use_traffic_flo_median_yn",
                "app_use_traffic_game",
                "app_use_traffic_game_median_yn",
                "app_use_traffic_healthcare",
                "app_use_traffic_healthcare_yn",
                "app_use_traffic_insta",
                "app_use_traffic_kakaostory",
                "app_use_traffic_melon",
                "app_use_traffic_melon_median_yn",
                "app_use_traffic_movie",
                "app_use_traffic_music",
                "app_use_traffic_music_median_yn",
                "app_use_traffic_music_ratio",
                "app_use_traffic_music_ratio_median",
                "app_use_traffic_music_ratio_median_yn",
                "app_use_traffic_naverband",
                "app_use_traffic_other_telco",
                "app_use_traffic_payment",
                "app_use_traffic_podcast",
                "app_use_traffic_public_tv",
                "app_use_traffic_public_tv_median_yn",
                "app_use_traffic_reward",
                "app_use_traffic_shopping_coupon",
                "app_use_traffic_shopping_median_yn",
                "app_use_traffic_shopping_parcel",
                "app_use_traffic_simple_pay",
                "app_use_traffic_stock",
                "app_use_traffic_svod",
                "app_use_traffic_travel",
                "app_use_traffic_twitter",
                "app_use_traffic_video",
                "app_use_traffic_video_clip",
                "app_use_traffic_video_median_yn",
                "app_use_traffic_video_ratio",
                "app_use_traffic_video_ratio_median",
                "app_use_traffic_video_ratio_median_yn",
                "app_use_traffic_wavve_median_yn",
                "app_use_traffic_youtube",
                "app_use_yn_11st_bf_m6",
                "app_use_yn_finnq_bf_m3",
                "app_use_yn_kdb_bf_m3",
                "avg_chg_duration",
                "avg_data_usage_in_gb",
                "avg_dcb_sml_pay_amt",
                "avg_display_resol",
                "avg_eqp_buy_duration",
                "avg_eqp_chg_duration",
                "avg_subscription_period",
                "avg_traffic_mb_per_hour",
                "bas_fee_amt",
                "bas_ofr_data_gb_qty_val",
                "bas_ofr_data_infinite_yn",
                "bf_1m_inv_amt",
                "bf_m3_data_over_usage_cnt",
                "bf_m3_fee_chg_cnt",
                "bf_m6_avg_data_usage_in_gb",
                "bf_m6_data_over_usage_cnt",
                "bf_m6_data_usage_ratio_avg",
                "bf_m6_sum_data_usage_in_gb",
                "campaign_acceptance_ratio_median_yn",
                "card_pay_cnt_bf_m0",
                "card_pay_cnt_bf_m1",
                "card_pay_cnt_bf_m2",
                "channel",
                "contact_baby_yn",
                "contact_homemove_yn",
                "contact_pet_yn",
                "context_businessman",
                "context_data_overuse",
                "context_data_use_weekend",
                "context_discount_benefit",
                "context_online_shopping",
                "copn_data_u1_yn_bf_m0",
                "copn_left_cnt_bf0",
                "copn_left_cnt_bf1",
                "copn_left_cnt_bf2",
                "data_gift_send_yn_bf_m0",
                "data_give_psbl_yn",
                "data_usage_in_gb_bf_m0",
                "data_usage_in_gb_bf_m1",
                "data_usage_in_gb_bf_m2",
                "data_usage_in_gb_bf_m3",
                "data_usage_in_gb_bf_m4",
                "data_usage_in_gb_bf_m5",
                "data_use_night_ratio",
                "data_use_night_ratio_median",
                "data_use_night_ratio_median_yn",
                "data_use_ratio_bf_m0",
                "data_use_ratio_bf_m1",
                "data_use_ratio_bf_m2",
                "data_use_ratio_familyshare",
                "data_use_ratio_max",
                "day_traffic_hour_ratio",
                "days_speed_limit",
                "dcb_amt_bf_m1_percent_rk",
                "eqp_chg_cnt",
                "eqp_chg_period",
                "eqp_chg_timing_days",
                "eqp_mdl_cd",
                "equip_chg_mth_cnt",
                "family_comb_duration",
                "family_comb_type",
                "family_rep_yn",
                "family_wire_comb_term_bf_m6_yn",
                "family_wire_comb_yn",
                "fee_chg_cnt",
                "fee_chg_period",
                "filter_adt_ansim_home_yn",
                "filter_agree_201",
                "filter_agree_203",
                "filter_aia_vitality",
                "filter_asgn_call_rgst_cust",
                "filter_chuck_for_tw",
                "filter_col",
                "filter_eqp_mdl_cd",
                "filter_fee_prod",
                "filter_five_g",
                "filter_frgnr",
                "filter_indv_corp_cl_cd",
                "filter_internet",
                "filter_lte",
                "filter_new_android_device",
                "filter_op_info_rejt_obj",
                "filter_pay_agr",
                "filter_pps",
                "filter_rep_mbr_ind",
                "filter_sex",
                "filter_sktemployee",
                "filter_smile",
                "filter_svc_cd",
                "filter_svc_st_cd",
                "filter_svc_use_typ_cd",
                "filter_term_dt",
                "filter_tfamilymoa",
                "filter_trnd_info_rejt_obj",
                "filter_usim_indpnd_svc",
                "filter_vas_booksdata",
                "filter_vcoloring_prod",
                "filter_welfare_discount",
                "filter_xcloud_prod",
                "five_g_device_yn",
                "last_display_resol",
                "last_eqp_buy_duration",
                "last_equip_period",
                "location_weekday_visit_city",
                "location_weekday_visit_dong",
                "location_weekday_visit_gu",
                "location_weekend_visit_city",
                "location_weekend_visit_dong",
                "location_weekend_visit_gu",
                "main_channel_eqp_buy",
                "max_display_resol",
                "mbr_card_gr_cd",
                "mbr_discount_amt_cum_bakery",
                "mbr_discount_amt_cum_beauty_and_fashion",
                "mbr_discount_amt_cum_chocolate",
                "mbr_discount_amt_cum_coffee",
                "mbr_discount_amt_cum_convenience_store",
                "mbr_discount_amt_cum_food_and_beverage",
                "mbr_discount_amt_cum_mobile_and_media",
                "mbr_discount_amt_cum_movie",
                "mbr_discount_amt_cum_shopping",
                "mbr_discount_amt_education",
                "mbr_discount_amt_family_restaurant",
                "mbr_discount_amt_jeju",
                "mbr_discount_amt_pizza",
                "mbr_discount_amt_sports",
                "mbr_discount_amt_theme_park",
                "mbr_discount_amt_transportation",
                "mbr_use_discount_amt_cum",
                "membership_amt_ratio_median_yn",
                "membership_cnt_ratio_median_yn",
                "membership_vip_yn",
                "mng_nice_cb_grd",
                "na00002040_yn",
                "na00004430_yn",
                "night_traffic_hour_ratio",
                "night_traffic_mb",
                "nm_chg_date_diff",
                "non_skt_wifi_use_yn",
                "non_vip_mbr_discount_median_yn",
                "nugu_app_rgst_yn",
                "nugu_dvc_rgst_yn",
                "nugu_user_yn",
                "pmth_inv_bamt",
                "prefer_device_manufacturer",
                "prefer_device_price",
                "prefer_discount_yn",
                "prefer_latest_device",
                "prefer_second_device_yn",
                "prod_nm",
                "real_arpu_bf_m1",
                "real_arpu_bf_m2",
                "real_arpu_bf_m3",
                "real_avg_arpu",
                "real_data_use_gb_bf_m0",
                "real_data_use_gb_bf_m1",
                "real_data_use_gb_bf_m2",
                "ref_data_usage_in_gb_bf_m0",
                "ref_data_usage_in_gb_bf_m1",
                "ref_data_usage_in_gb_bf_m2",
                "rem_allot_amt",
                "rem_allot_cnt",
                "roaming_cnt_m3",
                "sex_cd",
                "sml_pay_amt_bf_m1_percent_rk",
                "sms_rcv_cnt",
                "sms_rcv_cnt_interior",
                "sms_rcv_cnt_restaurant",
                "sms_snd_cnt",
                "svc_scrb_period",
                "tethering_traffic_mb",
                "tw_reco_page_healthhabit_bf15_imp_yn",
                "tw_tplan_chk_1m",
                "tw_visit_days_fee_median_yn",
                "tw_visit_days_fee_t_essence",
                "twd_device_nm",
                "vas_cnt_call",
                "vas_cnt_music",
                "vas_cnt_video",
                "voc_rcv_avg_duration",
                "voc_rcv_cnt",
                "voc_rcv_miss_cnt",
                "voc_rcv_prtn_cnt_bf_m0",
                "voc_rcv_prtn_cnt_bf_m1",
                "voc_rcv_prtn_cnt_bf_m2",
                "voc_snd_avg_duration",
                "voc_snd_cnt",
                "voc_snd_prtn_cnt_bf_m0",
                "voc_snd_prtn_cnt_bf_m1",
                "voc_snd_prtn_cnt_bf_m2",
                "voc_srv_cnt",
                "weekday_home_ldong_cd",
                "weekday_night_ldong_cd",
                "weekday_work_ldong_cd",
            ]
            assert pf_value not in all_val, "`pf_value`는 user profile 테이블(comm.user_profile_pivot)에 있는 값이어야 합니다."
        else:
            pf_value = None

        super().__init__([model], model_name, model_version, features)

        self.preprocess_logic = preprocess_logic
        self.postprocess_logic = postprocess_logic
        self.predict_fn = predict_fn
        self.data = data
        self.user_profile_nm = user_profile_nm
        self.pf_value = pf_value

    def predict(self, x: List[Any], **kwargs) -> Dict[str, Any]:
        pf_client = kwargs.get("pf_client") or MLSProfileAPIClient(runtime_env=MLSRuntimeENV.MMS)
        graph_client = kwargs.get("graph_client") or MLSGraphAPIClient(runtime_env=MLSRuntimeENV.MMS)
        dynamodb_client = kwargs.get("dynamodb_client") or DynamoDBClient(runtime_env=MLSRuntimeENV.MMS)

        preprocessed_x = self._preprocess(x, kwargs.get("keys", []), pf_client, graph_client, dynamodb_client)
        y = self._ml_predict(preprocessed_x)
        items = self._postprocess(x, kwargs.get("keys", []), y, pf_client, graph_client, dynamodb_client) or []

        return {"items": items}

    def _preprocess(
        self,
        x: List[Any],
        additional_keys: List[Any],
        pf_client: MLSProfileAPIClient,
        graph_client: MLSGraphAPIClient,
        dynamodb_client: DynamoDBClient,
    ) -> List[Any]:
        if len(self.features) != len(x):
            raise MLSModelError("GenericLogicModelCustom: `x`의 길이가 `features`의 길이와 다릅니다.")

        data = {name: x[i] for i, name in enumerate(self.features) if x[i] not in [None, []]}
        data["additional_keys"] = additional_keys
        data.update(self.data)

        try:
            return logic_processor.apply(
                self.preprocess_logic,
                data=data,
                pf_client=pf_client,
                graph_client=graph_client,
                dynamodb_client=dynamodb_client,
            )
        except Exception as e:
            raise MLSModelError(f"GenericLogicModelCustom: 전처리에 실패했습니다. {e}")

    def _ml_predict(self, preprocessed_x: List[Any]) -> Union[float, List[float], str, None]:
        try:
            if self.predict_fn == "none" and self.model_lib != "pytorch":
                return None

            if not isinstance(preprocessed_x[0], list):
                preprocessed_x = [preprocessed_x]

            if self.model_lib == "autogluon":
                input_data = DataFrame(
                    preprocessed_x, columns=[f for f in self.features if f not in self.non_training_features]
                )
            elif self.model_lib == "pytorch":
                input_data = torch.tensor(preprocessed_x, dtype=torch.float)
            else:
                input_data = np.array(preprocessed_x)

            if self.model_lib == "pytorch":
                y = self.models[0](input_data).detach().numpy()
            elif self.predict_fn == "predict":
                y = self.models[0].predict(input_data)
            else:
                y = self.models[0].predict_proba(input_data)
                if self.model_lib == "autogluon" and isinstance(y, DataFrame):
                    y = y.to_numpy()

            if len(y) == 1:
                y = y[0]

            try:
                return y.tolist()
            except AttributeError:
                return y

        except Exception as e:
            raise MLSModelError(f"GenericLogicModelCustom: ML Prediction에 실패했습니다. {e}")

    def _postprocess(
        self,
        x: List[Any],
        additional_keys: List[Any],
        y: Union[float, List[float], None],
        pf_client: MLSProfileAPIClient,
        graph_client: MLSGraphAPIClient,
        dynamodb_client: DynamoDBClient,
    ) -> List[Dict[str, Any]]:

        data = {name: x[i] for i, name in enumerate(self.features) if x[i] not in [None, []]}
        data["additional_keys"] = additional_keys
        data["y"] = y
        data.update(self.data)
        if self.pf_value:
            pf_values = pf_client.get_user_profile(
                profile_id=self.user_profile_nm, user_id=data["user_id"], keys=self.pf_value
            )

            data.update(pf_values)
        else:
            pass

        try:
            return self.postprocess_logic(data)
        except Exception as e:
            raise MLSModelError(f"GenericLogicModelCustom: 후처리에 실패했습니다. {e}")
