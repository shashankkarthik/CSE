#pragma once
#include "AudioNode.h"
class CAR :
	public CAudioNode
{
public:
	CAR();
	virtual ~CAR();

	void Start();

	bool Generate();

	void SetSource(CAudioNode * source) { m_source = source; };

private:
	double m_attack;
	double m_release;
	double m_duration;
	double m_time;

	CAudioNode *m_source;
};

